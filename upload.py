
import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

CLIENT_ID = os.environ["YOUTUBE_CLIENT_ID"]
CLIENT_SECRET = os.environ["YOUTUBE_CLIENT_SECRET"]
REFRESH_TOKEN = os.environ["YOUTUBE_REFRESH_TOKEN"]

VIDEO_FILE = "video.mp4"

if not os.path.exists(VIDEO_FILE):
    raise FileNotFoundError("video.mp4 not found in repository")

credentials = Credentials(
    token=None,
    refresh_token=REFRESH_TOKEN,
    token_uri="https://oauth2.googleapis.com/token",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    scopes=["https://www.googleapis.com/auth/youtube.upload"]
)

youtube = build("youtube", "v3", credentials=credentials)

request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": "Tiny Toons Hindi | Kids Song",
            "description": "Enjoy fun and entertaining kids songs with Tiny Toons Hindi!",
            "tags": ["Tiny Toons Hindi", "Kids Songs", "Hindi Rhymes"],
            "categoryId": "10"
        },
        "status": {
            "privacyStatus": "private",
            "selfDeclaredMadeForKids": True
        }
    },
    media_body=MediaFileUpload(VIDEO_FILE, resumable=True)
)

response = request.execute()
print("Video uploaded successfully:", response["id"])
