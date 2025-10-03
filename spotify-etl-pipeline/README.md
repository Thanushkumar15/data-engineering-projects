# Automated Spotify Playlist ETL Pipeline on AWS (Lambda + Glue + Athena)

This project automates the extraction, transformation, and loading (ETL) of Spotify playlist data into an AWS-based data lake.  
The pipeline fetches playlist metadata using the Spotify API, stores raw JSON files in Amazon S3, transforms them into structured Parquet format using AWS Glue (PySpark), and makes the data queryable using Athena.

---

## 🧠 Architecture Overview

| Step | Service | Description |
|------|---------|-------------|
| 1️⃣ Extraction | **AWS Lambda + Spotify API** | Lambda pulls playlist details (tracks, artists, albums) and stores raw JSON into S3. |
| 2️⃣ Storage | **Amazon S3 (Raw Zone)** | Raw API response is stored for traceability and auditing. |
| 3️⃣ Transformation | **AWS Glue (PySpark)** | JSON is flattened and converted to tabular format. |
| 4️⃣ Storage (Processed) | **Amazon S3 (Structured Zone)** | Cleaned dataset is written in Parquet format. |
| 5️⃣ Query & Analysis | **AWS Glue Crawler + Athena** | Crawlers update tables, and SQL queries can be run directly on playlist data. |

---

## 🏗️ Tech Stack

- **Python** (for Lambda ETL logic)
- **Spotify Web API**
- **AWS Lambda**
- **Amazon S3**
- **AWS Glue (PySpark)**
- **AWS Glue Crawler**
- **Amazon Athena**

---

## 📁 Project Structure

spotify-etl-pipeline/
│
├── src/
│ ├── lambda/
│ │ └── lambda_function.py
│ ├── glue/
│ │ └── spotify_transform.py
│
├── requirements.txt
├── .gitignore
└── README.md