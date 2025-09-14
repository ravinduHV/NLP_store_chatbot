#!/bin/bash

# Product Search Chatbot Launcher for Unix-like systems
# This script sets up the virtual environment, installs dependencies, and runs the chatbot

set -e  # Exit on any error

echo "Product Search Chatbot Setup"
echo "============================"

# Check if virtual environment exists, create if not
if [ ! -d "env" ]; then
    echo "Creating virtual environment..."
    python3 -m venv env
fi

# Activate virtual environment
echo "Activating virtual environment..."
source env/bin/activate

# Clear screen
clear

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# Clear screen
clear

# Run the chatbot
echo "Starting Product Search Chatbot..."
echo ""
python3 main.py