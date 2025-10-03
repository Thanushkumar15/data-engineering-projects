import os
import requests
import csv
import boto3
from dotenv import load_dotenv

# Load secrets
load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET_NAME = os.getenv("BUCKET_NAME")
OBJECT_NAME = "youtube/youtube_stats.csv"

video_ids = ['5uGzJSi--AM','Eo2kAkOHKzs','_1JbgiMm2xI']

def fetch_video_stats(video_id):
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&id={video_id}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if "items" in data and len(data["items"]) > 0:
        video_data = data["items"][0]
        snippet = video_data["snippet"]
        stats = video_data["statistics"]
        return {
            "video_id": video_id,
            "title": snippet["title"],
            "published_at": snippet["publishedAt"],
            "channel_title": snippet["channelTitle"],
            "views": stats.get("viewCount", 0),
            "likes": stats.get("likeCount", 0),
            "comments": stats.get("commentCount", 0),
        }
    else:
        return None

all_video_data = [fetch_video_stats(v) for v in video_ids if fetch_video_stats(v) is not None]

if all_video_data:
    csv_file = "youtube_stats.csv"
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=all_video_data[0].keys())
        writer.writeheader()
        writer.writerows(all_video_data)
    print("Data saved locally")

    s3 = boto3.client("s3",
                      aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                      region_name=AWS_REGION)
    try:
        s3.upload_file(csv_file, BUCKET_NAME, OBJECT_NAME)
        print("File uploaded to S3")
    except Exception as e:
        print(f"Upload failed: {e}")
else:
    print("No data to save")
