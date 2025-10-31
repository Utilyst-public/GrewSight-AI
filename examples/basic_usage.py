"""
Basic Usage Example - CrewSight-AI

© 2025 Utilyst Inc. All rights reserved.
"""

from src.crewsight.crew import CrewSightCrew


def main():
    """Run CrewSight-AI with basic configuration."""
    
    inputs = {
        'google_drive_url': 'https://drive.google.com/drive/folders/your_folder_id',
        'document_type': 'research_papers',
        'analysis_focus': 'key_findings',
        'output_format': 'summary'
    }
    
    print("Initializing CrewSight-AI...")
    crew = CrewSightCrew()
    
    print("Processing documents...")
    result = crew.crew().kickoff(inputs=inputs)
    
    print("\nComplete!")
    print(result)


if __name__ == "__main__":
    main()
