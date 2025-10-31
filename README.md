# CrewSight-AI — AI-Powered Document Processing System

**Owner:** Utilyst Inc.  
**Contact:** john@utilyst.com  
**© 2025 Utilyst Inc. All rights reserved.**

CrewSight-AI is a CrewAI-powered, multi-agent document processing system that retrieves, analyzes, and synthesizes documents from public Google Drive folders. Built with CrewAI 2.x, GPT-4o-mini, and Claude 3.5 Sonnet, it delivers comprehensive document analysis and reporting for research, compliance, and knowledge management workflows.

## 🧭 Overview

CrewSight-AI uses four coordinated AI agents to retrieve documents, analyze content, synthesize insights, and troubleshoot issues. It's designed for organizations that need to process large volumes of documents efficiently and extract actionable intelligence from unstructured data.

### Core Workflow

```
Google Drive Folder URL
        │
        ▼
Document Retriever (Custom Tool)
        │
        ▼
Document Analyzer (GPT-4o-mini)
        │
        ▼
Content Synthesizer (Claude 3.5 Sonnet)
        │
        ▼
Safety & Troubleshooting Agent (GPT-4o-mini)
        │
        ▼
Final Report (Markdown)
```

## 🤖 Agent Architecture

### Document Retriever
- **Tool:** PublicGoogleDriveProcessor
- **Function:** Fetches all accessible documents from public Google Drive folders
- **Output:** Catalog of retrieved files with metadata and download status

### Document Analyzer
- **Model:** GPT-4o-mini
- **Tools:** FileReadTool, SerperDevTool
- **Function:** Analyzes document content, structure, and extracts key information
- **Output:** Structured analysis with insights, patterns, and key findings

### Content Synthesizer
- **Model:** Claude 3.5 Sonnet
- **Function:** Creates comprehensive reports synthesizing information from multiple documents
- **Output:** Executive-ready markdown report with citations and recommendations

### Troubleshooting Agent
- **Model:** GPT-4o-mini
- **Function:** Monitors workflow, diagnoses issues, and ensures smooth operation
- **Output:** System health reports and issue resolution documentation

## ⚙️ Technical Architecture

- **Framework:** CrewAI 2.x (multi-agent orchestration)
- **Deployment:** CrewAI AMP, Docker, or local
- **Language:** Python 3.11+
- **LLMs:** OpenAI GPT-4o-mini, Anthropic Claude 3.5 Sonnet
- **Tools:** Custom Google Drive processor + file processing suite
- **Integration:** REST endpoints, CLI interface
- **Operation:** Works in cloud or on-premise environments

## 🚀 Installation

### Prerequisites

- Python 3.11+
- OpenAI API Key
- Anthropic API Key

### Setup

```bash
git clone https://github.com/Utilyst-public/CrewSight-AI.git
cd CrewSight-AI

# Option 1: Automated setup
./setup.sh  # Unix/macOS
# or
setup.bat   # Windows

# Option 2: Manual setup
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Configuration

```bash
cp .env.example .env
# Edit .env and add your API keys
```

```env
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key
```

## 🧪 Usage

### Local Test

```bash
python -m src.crewsight.main
```

### Example Input

Edit `src/crewsight/main.py`:

```python
inputs = {
    'google_drive_url': 'https://drive.google.com/drive/folders/your_folder_id',
    'document_type': 'research_papers',
    'analysis_focus': 'methodology_and_results',
    'output_format': 'detailed_report'
}
```

### Example Output

```
Google Drive Processing Complete
=================================

Folder ID: 1abc123def456
Total Files: 15
Successful Downloads: 15
Failed Downloads: 0

Analysis completed with 45 key insights extracted.
Final report saved to: output/final_report.md
```

## ☁️ Deployment on CrewAI AMP

```bash
# Log in
crewai login

# Deploy
crewai deploy create
```

Configuration is automatically read from `pyproject.toml`.  
The first build takes ~10–15 minutes. Subsequent pushes are near-instant.

## 🧱 Project Structure

```
crewsight-ai/
├── src/
│   └── crewsight/
│       ├── __init__.py
│       ├── main.py              # Entry point
│       ├── crew.py              # Agent orchestration
│       ├── config/
│       │   ├── agents.yaml      # Agent definitions
│       │   └── tasks.yaml       # Task definitions
│       └── tools/
│           └── public_google_drive_processor.py
├── tests/                       # Unit tests
├── examples/                    # Usage examples
├── docs/                        # Documentation
├── pyproject.toml              # Project configuration
├── requirements.txt            # Dependencies
├── .env.example               # Environment template
├── LICENSE                    # Proprietary license
├── NOTICE                     # Copyright notice
├── README.md                  # This file
└── PROJECT_OVERVIEW.md        # Detailed overview
```

## 🧰 Use Cases

### Research & Analysis
- Academic paper analysis and synthesis
- Market research document processing
- Competitive intelligence gathering
- Literature review automation

### Compliance & Legal
- Regulatory document analysis
- Policy document review
- Contract analysis and extraction
- Compliance reporting

### Knowledge Management
- Internal documentation processing
- Knowledge base creation
- Information extraction and indexing
- Cross-document relationship mapping

## 📊 Performance & Benefits

| Metric | Improvement |
|--------|-------------|
| Average execution time | 2–5 minutes |
| Document processing speed | 50–100 docs/hour |
| Manual analysis time saved | ↓ 80–90% |
| Cross-document synthesis | ↓ 5 hours → 10 minutes |
| Total time saved | ≈ 6–8 hours per project |

### Operational Impact

- Faster document processing and analysis
- Comprehensive insights from multiple sources
- Reduced manual research time
- Consistent analysis quality

## 🏗️ Technical Summary

| Component | Details |
|-----------|---------|
| Backend | Python + CrewAI 2.x |
| AI Models | GPT-4o-mini, Claude 3.5 Sonnet |
| Platform | CrewAI AMP, Docker, Local |
| Integration | REST APIs + CLI |
| Security | .env isolation, token-based auth |
| Deployment | GitHub → CrewAI AMP via OAuth |
| Scalability | Process 100+ documents concurrently |

## 🔒 Security & Privacy

- **Local Processing:** All document processing can run locally
- **API Key Security:** Environment variable isolation
- **Data Privacy:** No persistent storage of processed documents
- **Access Control:** Public folder access only (no authentication required)

## 🧪 Testing

```bash
# Run all tests
pytest

# With coverage
pytest --cov=src

# Specific tests
pytest tests/test_crew.py -v
```

## 🛠️ Development

### Adding New Agents

Edit `src/crewsight/config/agents.yaml` and `src/crewsight/crew.py`.

### Adding New Tools

Create new tool in `src/crewsight/tools/` and add to agents.

### Custom Configurations

Modify YAML files in `src/crewsight/config/` for behavior changes.

## 📚 Documentation

- **README.md** (this file) - Quick start and overview
- **PROJECT_OVERVIEW.md** - Detailed project information
- **QUICKSTART.md** - 5-minute setup guide
- **DEPLOYMENT.md** - Deployment options and guides
- **docs/ARCHITECTURE.md** - System architecture details
- **CONTRIBUTING.md** - Contribution guidelines

## 🧾 Ownership & Licensing

**All intellectual property in this repository** — including code, design, documentation, and workflows — **is owned exclusively by Utilyst Inc.**

This software is protected under a proprietary license.

**No rights are granted** to copy, distribute, or create derivative works without written consent from Utilyst Inc.

See **LICENSE** and **NOTICE** for full details.

For licensing inquiries, contact: **john@utilyst.com**

## 📞 Support

For issues, questions, or licensing inquiries:
- **Email:** john@utilyst.com
- **Company:** Utilyst Inc.

---

© 2025 Utilyst Inc. All rights reserved.
