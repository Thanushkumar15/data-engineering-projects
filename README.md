# **Data Engineering Projects**

This repository contains real-world ETL projects demonstrating Python, PySpark, AWS, and data pipeline skills. Each project includes data extraction, transformation, and loading workflows, showcasing cloud-based ETL automation and analytics.

## **Projects**
### **1. Spotify Playlist ETL Pipeline**

**Description:** Serverless ETL pipeline to fetch, transform, and store Spotify playlist data for analytics.

**Workflow:**

Fetch playlist data from Spotify API using AWS Lambda

Store raw JSON in Amazon S3

Transform and clean data using PySpark on AWS Glue

Store transformed data back into Amazon S3 (organized for analytics)

Query and analyze the transformed data using Amazon Athena

Automate execution using EventBridge for scheduled runs

Tech Stack: Python, PySpark, AWS Lambda, AWS Glue, Amazon S3, Athena, EventBridge

Folder: spotify-etl-pipeline

### **2. YouTube Channel Stats ETL Pipeline**

#### **Version 1: Local Script**

**Description:** Local ETL pipeline to collect YouTube channel stats and prepare data for analytics.

**Workflow:**

Fetch channel stats and video data using YouTube Data API

Clean and transform JSON → CSV

Upload CSV to Amazon S3 using Boto3

Query data using Amazon Athena

Tech Stack: Python, YouTube Data API, Boto3, Amazon S3, Athena

Folder: youtube-etl-pipeline/local-version

#### **Version 2: AWS Lambda**

**Description:** Serverless ETL pipeline to fetch YouTube channel stats and automate uploads.

**Workflow:**

Fetch channel stats and video data using YouTube Data API with AWS Lambda

Store raw JSON directly in Amazon S3

Transform and clean data using AWS Glue

Store transformed data in Amazon S3

Query and analyze data using Amazon Athena

Schedule automated runs using EventBridge

Tech Stack: Python, YouTube Data API, AWS Lambda, AWS Glue, Amazon S3, Athena, EventBridge

Folder: youtube-etl-pipeline/lambda-version

### ****3. Weather Data ETL Pipeline****

**Description:** Pipeline to fetch live weather data for multiple cities and make it analytics-ready.

**Workflow:**

Fetch live weather data using OpenWeatherMap API

Store raw data in CSV/JSON format in Amazon S3

Transform and clean data using AWS Glue

Query and analyze data using Amazon Athena

Tech Stack: Python, OpenWeatherMap API, AWS Glue, Amazon S3, Athena

Folder: weather-etl-pipeline