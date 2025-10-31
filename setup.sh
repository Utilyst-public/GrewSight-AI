#!/bin/bash
set -e

echo "================================================"
echo "CrewSight-AI Setup"
echo "© 2025 Utilyst Inc. All rights reserved."
echo "================================================"
echo ""

# Check Python
echo "Checking Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 required. Install Python 3.11+"
    exit 1
fi

python3 --version
echo ""

# Create venv
echo "Creating virtual environment..."
if [ -d "venv" ]; then
    echo "⚠️  venv exists. Skipping."
else
    python3 -m venv venv
    echo "✓ venv created"
fi
echo ""

# Activate and install
echo "Installing dependencies..."
source venv/bin/activate
pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet
echo "✓ Dependencies installed"
echo ""

# Create .env
if [ -f ".env" ]; then
    echo "⚠️  .env exists. Skipping."
else
    cp .env.example .env
    echo "✓ .env created"
    echo ""
    echo "⚠️  IMPORTANT: Edit .env and add your API keys!"
fi
echo ""

# Create directories
mkdir -p downloads output
echo "✓ Directories created"
echo ""

echo "================================================"
echo "Setup Complete! 🎉"
echo "================================================"
echo ""
echo "Next steps:"
echo "1. Edit .env with your API keys"
echo "2. Activate venv: source venv/bin/activate"
echo "3. Run: python -m src.crewsight.main"
echo ""
