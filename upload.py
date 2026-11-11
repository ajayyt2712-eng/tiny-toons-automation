
import os
import sys
import traceback

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

try:
    VIDEO_FILE = os.environ.get("VIDEO_PATH", "721.mp4")

    CLIENT_ID = os.environ["YOUTUBE_CLIENT_ID"]
    CLIENT_SECRET = os.environ["YOUTUBE_CLIENT_SECRET"]
    REFRESH_TOKEN = os.environ["YOUTUBE_REFRESH_TOKEN"]

    print("Checking video file...")

    if not os.path.isfile(VIDEO_FILE):
        raise FileNotFoundError(f"Video not found: {VIDEO_FILE}")

    print("Creating OAuth credentials...")

    credentials = Credentials(
        token=None,
        refresh_token=REFRESH_TOKEN,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        scopes=["https://www.googleapis.com/auth/youtube.upload"]
    )

    print("Refreshing access token...")
    credentials.refresh(Request())

    print("Connecting to YouTube...")

    youtube = build(
        "youtube",
        "v3",
        credentials=credentials
    )

    print("Starting video upload...")

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": "बच्चों का मजेदार गाना | Tiny Toons Hindi",
                "description": "बच्चों के लिए मजेदार हिंदी गाना। Tiny Toons Hindi में आपका स्वागत है!",
                "tags": [
                    "Tiny Toons Hindi",
                    "Kids Songs",
                    "Hindi Rhymes",
                    "Kids Videos"
                ],
                "categoryId": "10"
            },
            "status": {
                "privacyStatus": "private",
                "selfDeclaredMadeForKids": True
            }
        },
        media_body=MediaFileUpload(
            VIDEO_FILE,
            mimetype="video/mp4",
            resumable=True
        )
    )

    response = request.execute()

    print("YouTube upload successful!")
    print("Video ID:", response["id"])
    print("Video URL: https://www.youtube.com/watch?v=" + response["id"])

except Exception as error:
    print("UPLOAD FAILED!")
    print("Error type:", type(error).__name__)
    print("Error details:", str(error))
    traceback.print_exc()
    sys.exit(13)
