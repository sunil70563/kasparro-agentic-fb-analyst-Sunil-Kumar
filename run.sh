#!/bin/bash

# Kasparro Agentic Analyst Runner

# 1. Setup Env
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
else
    source .venv/bin/activate
fi

# 2. Run Pipeline
# Default query if none provided
QUERY="${1:-Why did ROAS drop and how can I fix the ads?}"

echo "Running Kasparro Analyst..."
echo "Query: $QUERY"

python src/run.py "$QUERY"