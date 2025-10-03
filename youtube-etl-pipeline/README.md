# YouTube Channel Stats ETL Pipeline

This project collects YouTube channel statistics and video data, then stores it in AWS for analysis.

## Project Overview
The ETL pipeline fetches video and channel stats from the YouTube Data API, cleans and stores the data as CSV in S3, and makes it queryable using Athena.

## Versions

### 1️⃣ Local Version
- Runs locally using Python
- Calls YouTube Data API
- Cleans JSON response and stores as CSV
- Uploads data to S3 using Boto3
- Secrets stored in `.env` (never pushed)

### 2️⃣ AWS Lambda Version
- Same ETL logic deployed on AWS Lambda
- Serverless and scheduled via CloudWatch/EventBridge
- Stores raw and processed data in S3
- Secrets handled via Lambda environment variables

## Tech Stack
- Python
- YouTube Data API
- AWS Lambda
- Amazon S3
- AWS Glue Crawler
- Amazon Athena

## Folder Structure
youtube-etl-pipeline/
├── README.md
├── local-version/
│ ├── main.py
│ ├── requirements.txt
│ └── .env.example
└── lambda-version/
├── lambda_function.py
├── requirements.txt
└── README.md