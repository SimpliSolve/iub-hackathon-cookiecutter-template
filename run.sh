#!/bin/bash
#=======================
# IUB Hackathon Cookiecutter Template
# Run full dummy pipeline
#=======================

echo "Running full dummy competition pipeline..."
bash train.sh
bash test.sh
echo "Full dummy pipeline execution completed."
