import os
import json

from google.oauth2.service_account import Credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/drive"]
SERVICE_CREDENTIALS_JSON = json.loads(os.environ["PMU_COW_SERVICE_CREDENTIALS"])

# configure credentials
creds = Credentials.from_service_account_info(
    info=SERVICE_CREDENTIALS_JSON, scopes=SCOPES
)


def main():
    try:
        # Create a DriveService object
        service = build("drive", "v3", credentials=creds)

        # Create a file metadata object. Specifies name of file.
        file_metadata = {"name": "clarinets.pdf"}

        # Create a media object. Specifies path to file.
        file_path = "/Users/owens/music-projects/python-music-utils/test-directory/test-dir1/clarinets.pdf"
        media = MediaFileUpload(file_path, mimetype="application/pdf")

        # Use the files().create() method to upload the file
        file = (
            service.files()
            .create(body=file_metadata, media_body=media, fields="id")
            .execute()
        )

        print(f'File ID: {file.get("id")}')

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()
