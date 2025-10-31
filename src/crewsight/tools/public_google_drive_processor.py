"""
Public Google Drive Processor Tool

Tool for accessing and processing documents from publicly shared Google Drive folders.

© 2025 Utilyst Inc. All rights reserved.
"""

import os
import re
import requests
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.parse import urlparse, parse_qs

from crewai_tools import BaseTool


class PublicGoogleDriveProcessorTool(BaseTool):
    """
    Tool for processing documents from public Google Drive folders.
    
    © 2025 Utilyst Inc. All rights reserved.
    """
    
    name: str = "Public Google Drive Processor"
    description: str = (
        "Access and download documents from publicly shared Google Drive folders. "
        "Provide a Google Drive folder URL and this tool will retrieve all accessible files. "
        "Returns a structured list of files with metadata and download status."
    )
    
    def __init__(self, download_dir: str = "./downloads"):
        """Initialize the Google Drive processor."""
        super().__init__()
        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(parents=True, exist_ok=True)
        
        self.list_api_url = "https://www.googleapis.com/drive/v3/files"
        self.download_url = "https://www.googleapis.com/drive/v3/files/{file_id}/export"
        self.direct_download_url = "https://drive.google.com/uc?export=download&id={file_id}"
    
    def _extract_folder_id(self, url: str) -> Optional[str]:
        """Extract the folder ID from a Google Drive URL."""
        folder_match = re.search(r'/folders/([a-zA-Z0-9_-]+)', url)
        if folder_match:
            return folder_match.group(1)
        
        parsed = urlparse(url)
        query_params = parse_qs(parsed.query)
        if 'id' in query_params:
            return query_params['id'][0]
        
        return None
    
    def _get_file_type(self, filename: str) -> str:
        """Determine file type from filename."""
        extension = Path(filename).suffix.lower()
        
        type_mapping = {
            '.pdf': 'PDF',
            '.doc': 'Word Document',
            '.docx': 'Word Document',
            '.xls': 'Excel Spreadsheet',
            '.xlsx': 'Excel Spreadsheet',
            '.ppt': 'PowerPoint',
            '.pptx': 'PowerPoint',
            '.txt': 'Text File',
            '.csv': 'CSV File',
            '.json': 'JSON File',
        }
        
        return type_mapping.get(extension, 'Unknown')
    
    def _list_files_in_folder(self, folder_id: str) -> List[Dict[str, Any]]:
        """List all files in a public Google Drive folder."""
        files = []
        
        try:
            folder_url = f"https://drive.google.com/drive/folders/{folder_id}"
            response = requests.get(folder_url, allow_redirects=True)
            
            if response.status_code == 200:
                content = response.text
                
                file_id_pattern = r'data-id="([a-zA-Z0-9_-]+)"'
                file_ids = re.findall(file_id_pattern, content)
                
                file_name_pattern = r'data-tooltip="([^"]+)"'
                file_names = re.findall(file_name_pattern, content)
                
                for file_id, file_name in zip(file_ids, file_names):
                    files.append({
                        'id': file_id,
                        'name': file_name,
                        'type': self._get_file_type(file_name),
                        'url': f"https://drive.google.com/file/d/{file_id}/view"
                    })
            
            return files
            
        except Exception as e:
            print(f"Error listing files: {str(e)}")
            return []
    
    def _download_file(self, file_id: str, file_name: str) -> Dict[str, Any]:
        """Download a file from Google Drive."""
        try:
            download_url = self.direct_download_url.format(file_id=file_id)
            response = requests.get(download_url, stream=True)
            
            if response.status_code == 200:
                file_path = self.download_dir / file_name
                
                with open(file_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                
                file_size = os.path.getsize(file_path)
                
                return {
                    'status': 'success',
                    'file_name': file_name,
                    'file_path': str(file_path),
                    'file_size': file_size,
                    'file_size_mb': round(file_size / (1024 * 1024), 2)
                }
            else:
                return {
                    'status': 'failed',
                    'file_name': file_name,
                    'error': f"HTTP {response.status_code}"
                }
                
        except Exception as e:
            return {
                'status': 'failed',
                'file_name': file_name,
                'error': str(e)
            }
    
    def _run(self, url: str) -> str:
        """Main execution method for the tool."""
        folder_id = self._extract_folder_id(url)
        
        if not folder_id:
            return "Error: Could not extract folder ID from URL."
        
        print(f"Processing folder: {folder_id}")
        
        files = self._list_files_in_folder(folder_id)
        
        if not files:
            return f"Warning: No files found in folder. Folder ID: {folder_id}"
        
        print(f"Found {len(files)} files")
        
        results = {
            'folder_id': folder_id,
            'folder_url': url,
            'total_files': len(files),
            'files': [],
            'successful_downloads': 0,
            'failed_downloads': 0
        }
        
        for file_info in files:
            print(f"Downloading: {file_info['name']}")
            download_result = self._download_file(file_info['id'], file_info['name'])
            
            file_info.update(download_result)
            results['files'].append(file_info)
            
            if download_result['status'] == 'success':
                results['successful_downloads'] += 1
            else:
                results['failed_downloads'] += 1
        
        summary = f"""
Google Drive Processing Complete
=================================

Folder ID: {folder_id}
Total Files: {results['total_files']}
Successful Downloads: {results['successful_downloads']}
Failed Downloads: {results['failed_downloads']}

Files Downloaded:
"""
        
        for file_info in results['files']:
            if file_info['status'] == 'success':
                summary += f"\n✓ {file_info['name']} ({file_info.get('file_size_mb', 0)} MB)"
            else:
                summary += f"\n✗ {file_info['name']} - Error: {file_info.get('error', 'Unknown')}"
        
        summary += f"\n\nAll files saved to: {self.download_dir}\n"
        
        return summary
