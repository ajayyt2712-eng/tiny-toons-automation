
import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

video_path = os.environ["VIDEO_PATH"]

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
            "title": "Hindi Kids Song | Tiny Toons Hindi",
            "description": "Enjoy fun Hindi kids songs!",
            "tags": ["Tiny Toons Hindi", "Kids Songs", "Hindi Rhymes"],
            "categoryId": "10"
        },
        "status": {
            "privacyStatus": "private",
            "selfDeclaredMadeForKids": True
        }
    },
    media_body=MediaFileUpload(
        video_path,
        chunksize=-1,
        resumable=True
    )
)

response = request.execute()
print("Video uploaded:", response["id"])
