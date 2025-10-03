import json
import base64
import boto3
import requests
import os

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("SPOTIFY_REFRESH_TOKEN", "")
PLAYLIST_ID = os.getenv("SPOTIFY_PLAYLIST_ID")

S3_BUCKET = os.getenv("SPOTIFY_S3_BUCKET")
S3_KEY_PREFIX = "raw/spotify_playlists/"

s3_client = boto3.client('s3')

def get_access_token():
    auth_header = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
    headers = {'Authorization': f'Basic {auth_header}', 'Content-Type': 'application/x-www-form-urlencoded'}

    if REFRESH_TOKEN:
        data = {'grant_type': 'refresh_token', 'refresh_token': REFRESH_TOKEN}
    else:
        data = {'grant_type': 'client_credentials'}

    response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
    response.raise_for_status()
    return response.json()['access_token']

def get_playlist(access_token, playlist_id):
    headers = {'Authorization': f'Bearer {access_token}'}
    url = f'https://api.spotify.com/v1/playlists/{playlist_id}'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def upload_to_s3(data, bucket, key):
    s3_client.put_object(Body=json.dumps(data), Bucket=bucket, Key=key)

def lambda_handler(event, context):
        access_token = get_access_token()
        playlist_data = get_playlist(access_token, PLAYLIST_ID)
        s3_key = f"{S3_KEY_PREFIX}playlist_{PLAYLIST_ID}.json"
        upload_to_s3(playlist_data, S3_BUCKET, s3_key)
        return {'statusCode': 200, 'body': json.dumps({'message': 'Playlist extracted and uploaded!'})}
