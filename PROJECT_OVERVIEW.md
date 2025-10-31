# Project Overview — CrewSight-AI

**Owner:** Utilyst Inc. • **Contact:** <john@utilyst.com> • **© 2025 Utilyst Inc. All rights reserved.**

CrewSight-AI is a **multimodal AI-powered document processing system** that retrieves, analyzes, and synthesizes documents from public Google Drive folders. Built with CrewAI 2.x, GPT-4o-mini, and Claude 3.5 Sonnet, it automates the entire workflow from document retrieval to comprehensive report generation.

##  What It Does

CrewSight-AI uses four specialized AI agents working together to:
1. **Retrieve** all documents from public Google Drive folders
2. **Analyze** document content to extract key insights
3. **Synthesize** information across multiple documents
4. **Generate** comprehensive, executive-ready reports

##  Agent Architecture

### Document Retriever
- **Tool:** PublicGoogleDriveProcessor
- **Function:** Fetches documents from public Google Drive folders
- **Output:** Catalog of files with metadata

### Document Analyzer  
- **Model:** Claude 3.5 Sonnet
- **Function:** Analyzes content and extracts insights
- **Output:** Structured analysis with key findings

### Content Synthesizer
- **Model:** GPT-4o-mini
- **Function:** Synthesizes information into cohesive reports
- **Output:** Executive-ready markdown report

## Technical Stack

- **Framework:** CrewAI 2.x (multi-agent orchestration)
- **Language:** Python 3.11+
- **LLMs:** OpenAI GPT-4o-mini, Anthropic Claude 3.5 Sonnet
- **Tools:** Custom Google Drive processor + file handling
- **Deployment:** Local, Docker, or CrewAI AMP

## Quick Start

```bash
# Clone repository
git clone https://github.com/Utilyst-public/CrewSight-AI.git
cd CrewSight-AI

# Setup (automated)
./setup.sh  # Unix/macOS
# or
setup.bat   # Windows

# Configure API keys
cp .env.example .env
# Edit .env with your keys

# Run
python -m src.crewsight.main
```

##  Use Cases

- **Research & Analysis:** Process academic papers and extract insights
- **Knowledge Management:** Build comprehensive knowledge bases
- **Compliance:** Analyze regulatory documents and policies
- **Market Intelligence:** Process competitive analysis documents

## Project Structure

```
crewsight-ai/
├── src/crewsight/          # Core application code
│   ├── main.py             # Entry point
│   ├── crew.py             # Agent orchestration
│   ├── config/             # YAML configurations
│   └── tools/              # Custom tools
├── tests/                  # Unit tests
├── examples/               # Usage examples
├── docs/                   # Documentation
├── requirements.txt        # Dependencies
├── pyproject.toml          # Project config
└── LICENSE                 # Proprietary license
```

## Security & Licensing

- **Proprietary software** owned by Utilyst Inc.
- No rights granted without written permission
- See **LICENSE** for full terms
- Contact: **john@utilyst.com** for licensing

## Documentation

- **README.md** - Quick start guide
- **QUICKSTART.md** - 5-minute setup
- **DEPLOYMENT.md** - Deployment options
- **docs/ARCHITECTURE.md** - Technical details

## Requirements

- Python 3.11+
- OpenAI API key
- Anthropic API key
- Public Google Drive folder URL

## Support

For questions, issues, or licensing inquiries:
- **Email:** john@utilyst.com
- **Company:** Utilyst Inc.

---

© 2025 Utilyst Inc. All rights reserved.
