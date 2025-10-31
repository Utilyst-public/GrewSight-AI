"""
CrewSight-AI API Layer

REST API endpoints for mobile app integration.
Connects mobile app to CrewAI agents for document processing.

© 2025 Utilyst Inc. All rights reserved.
"""

from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import uvicorn

from src.crewsight.crew import CrewSightCrew

app = FastAPI(
    title="CrewSight-AI API",
    description="Mobile app backend for AI-powered document processing",
    version="1.0.0"
)

# Request/Response Models
class IssueRequest(BaseModel):
    issue_description: str
    equipment_type: Optional[str] = None
    error_code: Optional[str] = None

class ProcessingRequest(BaseModel):
    google_drive_url: str
    document_type: str = "general"
    analysis_focus: str = "comprehensive_review"
    output_format: str = "structured_summary"

class ProcessingResponse(BaseModel):
    status: str
    session_id: str
    message: str
    result: Optional[dict] = None


# API Endpoints

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "service": "CrewSight-AI API",
        "status": "online",
        "version": "1.0.0",
        "owner": "Utilyst Inc."
    }


@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "agents": "ready",
        "api_version": "1.0.0"
    }


@app.post("/api/process/documents")
async def process_documents(request: ProcessingRequest):
    """
    Process documents from Google Drive
    
    Mobile app sends Google Drive URL and processing parameters.
    Returns processed insights and reports.
    """
    try:
        crew_instance = CrewSightCrew()
        
        inputs = {
            'google_drive_url': request.google_drive_url,
            'document_type': request.document_type,
            'analysis_focus': request.analysis_focus,
            'output_format': request.output_format
        }
        
        result = crew_instance.crew().kickoff(inputs=inputs)
        
        return ProcessingResponse(
            status="success",
            session_id="session_123",  # Generate proper session ID
            message="Document processing completed",
            result={"output": str(result)}
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/analyze/issue")
async def analyze_issue(request: IssueRequest):
    """
    Analyze equipment issue
    
    Mobile app sends issue description for AI analysis.
    Returns troubleshooting guidance.
    """
    try:
        # Placeholder for issue analysis logic
        # This would integrate with vision_analyzer agent
        
        return {
            "status": "success",
            "analysis": "Issue analysis completed",
            "recommendations": [
                "Check power connections",
                "Verify network settings",
                "Inspect for physical damage"
            ]
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/upload/image")
async def upload_image(file: UploadFile = File(...)):
    """
    Upload equipment image for analysis
    
    Mobile app sends photo for vision-based troubleshooting.
    """
    try:
        contents = await file.read()
        
        # Save file temporarily
        # Process with vision_analyzer agent
        
        return {
            "status": "success",
            "message": "Image uploaded and analyzed",
            "filename": file.filename,
            "analysis": "Image analysis placeholder"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/session/{session_id}")
async def get_session(session_id: str):
    """
    Retrieve session details
    
    Mobile app fetches session history and results.
    """
    return {
        "session_id": session_id,
        "status": "completed",
        "created_at": "2025-10-30T10:00:00Z",
        "issue_type": "Network Connectivity",
        "resolution_time": "15 minutes"
    }


@app.get("/api/sessions/recent")
async def get_recent_sessions(limit: int = 10):
    """
    Get recent troubleshooting sessions
    
    Mobile app displays user's session history.
    """
    return {
        "sessions": [
            {
                "session_id": "session_001",
                "issue": "Router not responding",
                "status": "resolved",
                "timestamp": "2025-10-30T09:00:00Z"
            }
        ]
    }


if __name__ == "__main__":
    print("=" * 70)
    print("🚀 CrewSight-AI API Server")
    print("=" * 70)
    print("© 2025 Utilyst Inc. All rights reserved.")
    print()
    print("Starting server at http://localhost:8000")
    print("API docs available at http://localhost:8000/docs")
    print()
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
