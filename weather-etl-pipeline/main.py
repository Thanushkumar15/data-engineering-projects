import os
import csv
import requests
import boto3
from dotenv import load_dotenv

# Load secrets
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET_NAME = os.getenv("BUCKET_NAME")
OBJECT_NAME = os.getenv("OBJECT_NAME")

cities = ["Hyderabad", "Bengaluru", "Mumbai"]

csv_file = "weather_data.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["City", "Weather Main", "Description", "Temp (°C)", "Humidity (%)", "Wind Speed (m/s)"])

    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        city_name = data.get("name")
        weather_main = data["weather"][0]["main"]
        weather_desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        writer.writerow([city_name, weather_main, weather_desc, temp, humidity, wind_speed])

# Upload to S3
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

try:
    s3.upload_file(csv_file, BUCKET_NAME, OBJECT_NAME)
    print("Weather CSV uploaded to S3")
except Exception as e:
    print(f"Upload failed: {e}")
