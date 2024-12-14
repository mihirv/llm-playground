
#!/bin/bash

# Create virtual environment
python3 -m venv llm-play

# Activate virtual environment
source llm-play/bin/activate

# Install dependencies
pip install -r requirements.txt