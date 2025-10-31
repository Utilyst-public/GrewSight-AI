#!/usr/bin/env python
"""
CrewSight-AI - Main Entry Point

AI-powered document processing system for analyzing documents from
public Google Drive folders.

© 2025 Utilyst Inc. All rights reserved.
"""

import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.crewsight.crew import CrewSightCrew


def run():
    """
    Run the CrewSight-AI document processor.
    
    This function initializes the crew and kicks off the document processing
    workflow with default or custom inputs.
    """
    print("=" * 70)
    print("🚀 CrewSight-AI - Document Processing System")
    print("=" * 70)
    print("© 2025 Utilyst Inc. All rights reserved.")
    print()
    
    # Example inputs - customize these based on your needs
    inputs = {
        'google_drive_url': 'https://drive.google.com/drive/folders/your_folder_id_here',
        'document_type': 'general',
        'analysis_focus': 'comprehensive_review',
        'output_format': 'structured_summary'
    }
    
    print("📋 Configuration:")
    for key, value in inputs.items():
        print(f"   {key}: {value}")
    print()
    
    try:
        # Initialize the crew
        crew_instance = CrewSightCrew()
        
        print("🤖 Initializing agents...")
        crew = crew_instance.crew()
        
        print("⚙️  Starting document processing...")
        print()
        
        # Kick off the crew with inputs
        result = crew.kickoff(inputs=inputs)
        
        print()
        print("=" * 70)
        print("✅ Processing Complete!")
        print("=" * 70)
        print()
        print("📊 Results:")
        print(result)
        print()
        
        return result
        
    except Exception as e:
        print()
        print("=" * 70)
        print("❌ Error occurred during processing")
        print("=" * 70)
        print(f"Error: {str(e)}")
        print()
        print("💡 Troubleshooting tips:")
        print("   1. Check your .env file contains valid API keys")
        print("   2. Ensure the Google Drive URL is publicly accessible")
        print("   3. Verify all dependencies are installed: pip install -r requirements.txt")
        print("   4. Check the logs for detailed error information")
        print()
        sys.exit(1)


def train():
    """Train the crew for the given number of iterations."""
    print("=" * 70)
    print("🎓 Training CrewSight-AI Crew")
    print("=" * 70)
    print()
    
    inputs = {
        "google_drive_url": "https://drive.google.com/drive/folders/sample_folder",
        "document_type": "training_data",
        "analysis_focus": "learning_optimization",
        "output_format": "training_summary"
    }
    
    try:
        crew_instance = CrewSightCrew()
        crew_instance.crew().train(
            n_iterations=int(sys.argv[2]) if len(sys.argv) > 2 else 5,
            filename=sys.argv[3] if len(sys.argv) > 3 else "training_data.pkl",
            inputs=inputs
        )
        
        print()
        print("✅ Training completed successfully!")
        print()
        
    except Exception as e:
        print(f"❌ Training failed: {str(e)}")
        sys.exit(1)


def replay():
    """Replay the crew execution from a specific task."""
    print("=" * 70)
    print("🔄 Replaying CrewSight-AI Crew")
    print("=" * 70)
    print()
    
    try:
        crew_instance = CrewSightCrew()
        crew_instance.crew().replay(task_id=sys.argv[2])
        
        print()
        print("✅ Replay completed successfully!")
        print()
        
    except Exception as e:
        print(f"❌ Replay failed: {str(e)}")
        sys.exit(1)


def test():
    """Test the crew execution and returns the results."""
    print("=" * 70)
    print("🧪 Testing CrewSight-AI Crew")
    print("=" * 70)
    print()
    
    inputs = {
        "google_drive_url": "https://drive.google.com/drive/folders/test_folder",
        "document_type": "test_documents",
        "analysis_focus": "quick_test",
        "output_format": "test_summary"
    }
    
    try:
        crew_instance = CrewSightCrew()
        crew_instance.crew().test(
            n_iterations=int(sys.argv[2]) if len(sys.argv) > 2 else 3,
            openai_model_name=sys.argv[3] if len(sys.argv) > 3 else "gpt-4",
            inputs=inputs
        )
        
        print()
        print("✅ Testing completed successfully!")
        print()
        
    except Exception as e:
        print(f"❌ Testing failed: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    # Check if a specific command was provided
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "train":
            train()
        elif command == "replay":
            if len(sys.argv) < 3:
                print("❌ Error: Task ID required for replay")
                print("Usage: python -m src.crewsight.main replay <task_id>")
                sys.exit(1)
            replay()
        elif command == "test":
            test()
        else:
            print(f"❌ Unknown command: {command}")
            print("Available commands: train, replay, test")
            sys.exit(1)
    else:
        # Run the default workflow
        run()
