import json
import csv
import requests
import boto3
import os


def lambda_handler(event, context):
    API_KEY = os.environ["YOUTUBE_API_KEY"]
    video_ids = ['_AoO-0YC_jU', 'ep9J7Kl2t8A']
    video_id_str = ','.join(video_ids)

    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&id={video_id_str}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    csv_file = "/tmp/video_stats.csv"
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Views", "Likes"])
        for item in data["items"]:
            writer.writerow([item["snippet"]["title"],
                             item["statistics"]["viewCount"],
                             item["statistics"]["likeCount"]])

    s3 = boto3.client('s3')
    bucket_name = os.environ["BUCKET_NAME"]
    s3.upload_file(csv_file, bucket_name, "video_stats.csv")

    return {
        'statusCode': 200,
        'body': json.dumps('CSV uploaded successfully!')
    }
