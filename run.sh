#!/bin/bash

# Activate virtual environment
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
elif [ -f "venv/Scripts/activate" ]; then
    source venv/Scripts/activate
fi

#=======================
# IUB Hackathon Cookiecutter Template
# Run full dummy pipeline
#=======================

echo "Running full dummy competition pipeline..."
python main.py
echo "Full dummy pipeline execution completed."
