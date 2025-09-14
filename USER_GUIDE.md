# Product Search Chatbot User Guide

## Overview

The Product Search Chatbot is an intelligent shopping assistant that helps customers find products in a grocery store using natural language processing. The chatbot analyzes your shopping requests and provides shelf locations for the products you're looking for.

## Features

- **Natural Language Processing**: Understands everyday shopping language
- **Product Search**: Searches through a comprehensive product database
- **Shelf Location Guidance**: Provides exact shelf locations for found products
- **Multi-Category Support**: Supports fruits, vegetables, dairy, meat, cleaning supplies, and more
- **Real-time Results**: Instant search results with organized output

## Getting Started

### Prerequisites

**System Requirements:**
- Python 3.7 or higher
- Operating System: Windows, Linux, or macOS
- Internet connection (required for initial setup to download NLP models)
- At least 2GB free disk space (for NLP model downloads)

**Software Dependencies:**
- pip (Python package installer)
- Virtual environment support (included with Python 3.7+)

**Note:** The application will automatically download required NLP models (NLTK data and spaCy English model) on first run if not already present.

### Installation

1. **Clone or download the project** to your local machine
2. **Navigate to the project directory**:
   ```powershell
   cd "D:\efac\CO sem 5\NLP\chatbot"
   ```
3. **Run the appropriate setup script**:

   **For Windows (PowerShell):**
   ```powershell
   .\run.ps1
   ```

   **For Unix/Linux/macOS:**
   ```bash
   chmod +x run.sh
   ./run.sh
   ```

   **For Windows with Git Bash or WSL:**
   ```bash
   bash run.sh
   ```

   These scripts will:
   - Create a virtual environment (if it doesn't exist)
   - Activate the virtual environment
   - Install all required dependencies
   - Launch the chatbot

## How to Use

### Starting the Chatbot

After running the setup, you'll see:
```
Enter a sentence (or 'exit'/'ctrl+c' to quit):
```

### Making Queries

Type your shopping request in natural language. Examples:

- "I want to buy apples and milk"
- "Where can I find detergent?"
- "I'm looking for bread, eggs, and bananas"
- "Do you have chicken and fish?"

### Understanding Results

The chatbot will display:

1. **Named Entities**: Any recognized entities in your query
2. **Product Results**: A table showing products and their shelf locations
3. **Summary**: Total number of items found

Example output:
```
Products            Shelf Location
________            ______________
apple               |A1
milk                |B3
detergent           |C2

3 Items Found
```

### Exiting the Chatbot

- Type `exit` and press Enter
- Press `Ctrl+C` to force quit

## Tips for Better Results

1. **Be Specific**: Use exact product names when possible
2. **Use Natural Language**: Write as you would speak ("I need milk and bread")
3. **Multiple Items**: List multiple products in one query
4. **Categories**: Mention categories if product names are unclear
5. **Singular/Plural**: Both forms work (apple/apples, egg/eggs)

## Troubleshooting

### Getting Help

If you encounter issues:
1. Check that all dependencies are installed
2. Verify Python version (3.7+)
3. Ensure you're in the correct directory
4. Try running the setup script again

## Technical Details

- **Language**: Python 3.7+
- **NLP Libraries**: NLTK, spaCy
- **Data Storage**: JSON format
- **Interface**: Command-line
- **Platform**: Windows (PowerShell)

