#!/bin/bash

echo "Setting up OmniBot..."

# Ensure Python is installed
if ! command -v python3 &>/dev/null; then
    echo "Python3 not found. Please install it first."
    exit 1
fi

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialize database
python3 core/database.py

echo "Setup complete! Run 'python3 core/omnibot.py' to start the bot."
