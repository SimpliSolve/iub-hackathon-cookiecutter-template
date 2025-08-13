#!/bin/bash
#=======================
# IUB Hackathon Cookiecutter Template
# Full setup for Linux/macOS + Windows Git Bash/WSL
#=======================

# Function to check command existence
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Step 0: Check Python
if ! command_exists python3 && ! command_exists python; then
    echo "Python is not installed. Please install Python 3 first."
    exit 1
fi

# Step 1: Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv 2>/dev/null || python -m venv venv
else
    echo "Virtual environment already exists."
fi

# Step 2: Make all scripts executable
echo "Making bash scripts executable..."
chmod +x *.sh || true
find . -name "*.sh" -exec chmod +x {} \; || true

# Step 3: Activate virtual environment
if [ -f "venv/bin/activate" ]; then
    echo "Activating virtual environment (Linux/macOS)..."
    source venv/bin/activate
elif [ -f "venv/Scripts/activate" ]; then
    echo "Activating virtual environment (Windows)..."
    source venv/Scripts/activate
else
    echo "Cannot find virtual environment activation script!"
    exit 1
fi

# Step 4: Upgrade pip and install dependencies
echo "Installing requirements..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete!"
echo "To run the pipeline, use:"
echo "  bash run.sh"

# Keep the virtual environment active for this session
$SHELL
