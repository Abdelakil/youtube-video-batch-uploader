# YouTube Video Batch Uploader

This Python script allows you to upload videos to YouTube using the YouTube Data API. It automates the process of authenticating, authorizing, and uploading videos to your YouTube account. After uploading, it also deletes the video files locally.

## Prerequisites

Before running the script, ensure that you have the following:

1. **Google Cloud Platform project**: Create a project in the Google Cloud Platform Console and enable the YouTube Data API.
2. **Client secrets file**: Download the client secrets JSON file from the Google Cloud Platform Console. Rename the file to `client_secret.json` and place it in the same directory as the script.
3. **Python environment**: Make sure you have Python installed on your system.

## Setup

1. **Install Dependencies**: Run the following command to install the required dependencies:

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

2. **Configure OAuth Credentials**:
- Replace the `client_secret.json` file in the script with your own client secrets file.
- Update the `redirect_uri` parameter in the `InstalledAppFlow.from_client_secrets_file()` method with your desired redirect URI.

## Usage

1. **Specify Folder Paths**: Update the `folder_paths` list with the paths to the folders containing the videos you want to upload. Ensure that the folder names are correct and the video files have the `.mp4` extension.

2. **Run the Script**: Execute the script using Python. It will authenticate and authorize access to your YouTube account, upload the videos from the specified folders to YouTube, and delete the uploaded video files locally.

## Note

- The script uses the YouTube Data API to upload videos. Make sure you have enabled the YouTube Data API for your Google Cloud Platform project.
- The privacy status of the uploaded videos is set to "public" by default. Modify the `'privacyStatus'` parameter in the `status` section of the video upload request if you want a different privacy setting.
- The script assumes that you have the necessary permissions to upload videos to your YouTube account. Make sure your YouTube account has the required privileges.
- The script will delete the uploaded video files locally after successful upload. Make sure to have proper backups or copies of the video files before running the script.

## Disclaimer

Use this script responsibly and in compliance with YouTube's terms of service. Ensure that you have the necessary rights and permissions to upload the videos you intend to upload. The script is provided as-is, and the authors take no responsibility for any misuse or unauthorized actions performed with this script.

**Note**: The script provided here is a simplified example and may require additional error handling, authentication token refreshing, or other improvements based on your specific requirements and use case.
