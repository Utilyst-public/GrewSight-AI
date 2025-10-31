# Quick Start Guide - CrewSight-AI

Get CrewSight-AI running in 5 minutes!

© 2025 Utilyst Inc. All rights reserved.

## Prerequisites

- Python 3.11+
- Git
- OpenAI and Anthropic API keys

## Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/Utilyst-public/CrewSight-AI.git
cd CrewSight-AI
```

### Step 2: Run Setup Script

**On Unix/macOS:**
```bash
chmod +x setup.sh
./setup.sh
```

**On Windows:**
```bash
setup.bat
```

### Step 3: Configure API Keys

```bash
cp .env.example .env
# Edit .env and add your keys
```

Add your actual API keys:
```env
OPENAI_API_KEY=sk-your-actual-key
ANTHROPIC_API_KEY=sk-ant-your-actual-key
```

## Run It!

```bash
python -m src.crewsight.main
```

## Customize

Edit `src/crewsight/main.py` to change the Google Drive folder:

```python
inputs = {
    'google_drive_url': 'https://drive.google.com/drive/folders/YOUR_FOLDER_ID',
    'document_type': 'research_papers',
    'analysis_focus': 'key_findings'
}
```

## Troubleshooting

**"Module not found"**
→ Run: `pip install -r requirements.txt`

**"Invalid API key"**
→ Check your `.env` file

**"Folder not accessible"**
→ Ensure folder is set to "Anyone with the link can view"

## What's Next?

- Read **README.md** for full documentation
- Check **examples/** for usage patterns
- Review **docs/ARCHITECTURE.md** for technical details

---

Ready to process documents! 🚀

© 2025 Utilyst Inc. All rights reserved.
