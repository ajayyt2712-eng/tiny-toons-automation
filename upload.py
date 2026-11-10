
import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials
VIDEO_FILE = "721.mp4"

credentials = Credentials(
    token=None,
    refresh_token=os.environ["YOUTUBE_REFRESH_TOKEN"],
    token_uri="https://oauth2.googleapis.com/token",
    client_id=os.environ["YOUTUBE_CLIENT_ID"],
    client_secret=os.environ["YOUTUBE_CLIENT_SECRET"],
    scopes=["https://www.googleapis.com/auth/youtube.upload"]
)

youtube = build("youtube", "v3", credentials=credentials)

request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": "बच्चों का मजेदार गाना | Tiny Toons Hindi",
            "description": "बच्चों के लिए मजेदार हिंदी गाना। Tiny Toons Hindi को Subscribe करें!",
            "tags": ["Kids Songs", "Hindi Rhymes", "Kids Videos", "Tiny Toons Hindi"],
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
print("Video uploaded successfully!")
print("Video ID:", response["id"])
