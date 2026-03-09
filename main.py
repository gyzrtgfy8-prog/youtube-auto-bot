import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.upload"]

api_service_name = "youtube"
api_version = "v3"

flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    "credentials.json", scopes)

credentials = flow.run_console()

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, credentials=credentials)

request_body = {
    "snippet": {
        "categoryId": "22",
        "title": "My AI Generated Video",
        "description": "Uploaded automatically",
        "tags": ["ai", "automation", "youtube bot"]
    },
    "status": {
        "privacyStatus": "public"
    }
}

request = youtube.videos().insert(
    part="snippet,status",
    body=request_body,
    media_body="video.mp4"
)

response = request.execute()

print("Video uploaded!")
