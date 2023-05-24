import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.http import MediaFileUpload

# Authenticate and authorize access
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    'client_secret.json',
    scopes=['https://www.googleapis.com/auth/youtube.upload'],
    redirect_uri='http://localhost:8080/'
)
credentials = flow.run_local_server(port=8080, prompt='consent')

# Get the access token
youtube = googleapiclient.discovery.build('youtube', 'v3', credentials=credentials)

# Folder paths
folder_paths = ["folder_example1", "folder_example2"]

for folder_path in folder_paths:
    # Get the folder name
    folder_name = os.path.basename(folder_path)

    # Iterate through the video files in the folder
    for filename in os.listdir(folder_path):
        # Construct the video path
        video_path = os.path.join(folder_path, filename)

        # Upload the video to YouTube
        request = youtube.videos().insert(
            part='snippet,status',
            body={
                'snippet': {
                    'title': folder_name + ' - ' + "quote.",
                    'description': 'Follow @AIQuotesGPT for more quotes',
                },
                'status': {
                    'privacyStatus': 'public'  # Change the privacy status as needed
                }
            },
            media_body=MediaFileUpload(video_path)
        )
        response = request.execute()
        print('Video uploaded successfully.')
        
        # Delete the uploaded video file locally
        os.remove(video_path)
        print('Video deleted locally.')

