#!/bin/bash
set -e
echo "Starting InsightStream: Real-Time Sentiment Analysis and Visualization..."
uvicorn app:app --host 0.0.0.0 --port 9000 --workers 1
