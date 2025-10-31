"""
CrewSight-AI Crew

Multi-agent orchestration for document processing from public Google Drive folders.

© 2025 Utilyst Inc. All rights reserved.
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool, SerperDevTool

from src.crewsight.tools.public_google_drive_processor import PublicGoogleDriveProcessorTool


@CrewBase
class CrewSightCrew:
    """
    CrewSight-AI Document Processing Crew
    
    A multi-agent system designed to retrieve, analyze, and process
    documents from public Google Drive folders.
    
    © 2025 Utilyst Inc. All rights reserved.
    """
    
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    def __init__(self):
        """Initialize the crew with necessary tools and configurations."""
        self.file_read_tool = FileReadTool()
        self.serper_tool = SerperDevTool()
        self.google_drive_tool = PublicGoogleDriveProcessorTool()
    
    @agent
    def document_retriever(self) -> Agent:
        """
        Document Retriever Agent
        
        Specialized in retrieving documents from public Google Drive folders.
        
        Returns:
            Agent: Configured document retriever agent
        """
        return Agent(
            config=self.agents_config['document_retriever'],
            tools=[self.google_drive_tool],
            verbose=True
        )
    
    @agent
    def document_analyzer(self) -> Agent:
        """
        Document Analyzer Agent
        
        Analyzes retrieved documents to extract insights and key information.
        
        Returns:
            Agent: Configured document analyzer agent
        """
        return Agent(
            config=self.agents_config['document_analyzer'],
            tools=[self.file_read_tool, self.serper_tool],
            verbose=True
        )
    
    @agent
    def content_synthesizer(self) -> Agent:
        """
        Content Synthesizer Agent
        
        Synthesizes information from multiple documents into comprehensive reports.
        
        Returns:
            Agent: Configured content synthesizer agent
        """
        return Agent(
            config=self.agents_config['content_synthesizer'],
            tools=[self.file_read_tool],
            verbose=True
        )
    
    @task
    def retrieve_documents_task(self) -> Task:
        """
        Retrieve Documents Task
        
        Task for retrieving all accessible documents from the specified
        Google Drive folder.
        
        Returns:
            Task: Configured document retrieval task
        """
        return Task(
            config=self.tasks_config['retrieve_documents'],
            agent=self.document_retriever()
        )
    
    @task
    def analyze_documents_task(self) -> Task:
        """
        Analyze Documents Task
        
        Task for analyzing the content and structure of retrieved documents.
        
        Returns:
            Task: Configured document analysis task
        """
        return Task(
            config=self.tasks_config['analyze_documents'],
            agent=self.document_analyzer()
        )
    
    @task
    def synthesize_content_task(self) -> Task:
        """
        Synthesize Content Task
        
        Task for synthesizing information from multiple documents into
        a cohesive report.
        
        Returns:
            Task: Configured content synthesis task
        """
        return Task(
            config=self.tasks_config['synthesize_content'],
            agent=self.content_synthesizer(),
            output_file='output/final_report.md'
        )
    
    @crew
    def crew(self) -> Crew:
        """
        Create and configure the CrewSight-AI Crew
        
        Assembles all agents and tasks into a cohesive crew that works
        together to process documents from Google Drive.
        
        Returns:
            Crew: Fully configured crew ready for execution
        """
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # Optional: Configure memory and planning
            memory=True,
            planning=True,
            # Optional: Add custom configurations
            manager_llm="gpt-4",  # For hierarchical process
            max_rpm=30,  # Rate limiting
        )
