# YouTube ETL Lambda Version

This is the serverless version of the YouTube ETL pipeline.

## Overview
- Fetches YouTube video statistics via YouTube Data API
- Generates a CSV and uploads it to S3
- Runs on AWS Lambda
- Scheduled via CloudWatch/EventBridge

## Setup
1. Create a Lambda function in AWS.
2. Set environment variables:
   - `YOUTUBE_API_KEY`
   - `BUCKET_NAME`
3. Upload `lambda_function.py` and package dependencies (`requests`, `boto3`).
4. Set permissions for Lambda to access S3.

## Folder Structure
lambda-version/
├── lambda_function.py
├── requirements.txt
└── README.md