Weather Data ETL Pipeline

This project collects live weather data from OpenWeatherMap API and stores it in AWS for analysis.

Project Description

Collects live weather data for multiple cities using OpenWeatherMap API (Python).

Saves data as CSV and uploads it to Amazon S3 using Boto3.

Uses AWS Glue Crawler to organize the data and makes it queryable using Amazon Athena.

Tech Stack

Python

OpenWeatherMap API

Amazon S3

Boto3

AWS Glue Crawler

Amazon Athena

Folder Structure
weather-etl-pipeline/
│
├── README.md
├── requirements.txt
├── .gitignore
├── .env
├── main.py