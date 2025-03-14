#!/bin/bash

echo "🚀 Setting up OmniBot..."

# Ensure Python is installed
if ! command -v python3 &>/dev/null; then
    echo "❌ Python3 not found. Please install it first."
    exit 1
fi

# Create virtual environment
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate

# Install dependencies
if [ -f "requirements.txt" ]; then
    echo "📦 Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "❌ requirements.txt not found! Ensure it's in the root directory."
    exit 1
fi

# Initialize database
if [ -f "core/database.py" ]; then
    echo "🗄 Initializing database..."
    python3 core/database.py
else
    echo "⚠️ Database script not found! Skipping database setup."
fi

# Start OmniBot
if [ -f "core/omnibot.py" ]; then
    echo "🚀 Starting OmniBot..."
    nohup python3 core/omnibot.py > omnibot.log 2>&1 &
    echo "✅ OmniBot is now running in the background. View logs with 'tail -f omnibot.log'"
else
    echo "❌ OmniBot script not found! Ensure core/omnibot.py exists."
    exit 1
fi
