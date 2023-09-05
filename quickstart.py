# from __future__ import print_function

import os
from sys import argv
import json

from google.auth.transport.requests import Request

from google.oauth2.credentials import Credentials

from google_auth_oauthlib.flow import InstalledAppFlow

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

""" If modifying the scope, delete file 'token.json'. """
# SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly"]
# SCOPES = ["https://www.googleapis.com/auth/drive"]

# Allows app to view/manage only files and folders that it has created
SCOPES = [
    "https://www.googleapis.com/auth/drive.file",
]

""" As of now, app will only work on my machine because credentials are only on my machine. """
USER_CREDENTIALS_JSON = json.loads(os.environ["PMU_COW_USER_CREDENTIALS"])


def main(part_name):
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None

    # The below is for user account authentication...
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        # for service account
        # creds = Credentials.from_service_account_file("token.json", scopes=SCOPES)

        # for user account
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            # for service account => FIX <=
            # flow = InstalledAppFlow.from_client_config(SERVICE_CREDENTIALS_JSON, SCOPES)

            # for user account
            # flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            flow = InstalledAppFlow.from_client_config(USER_CREDENTIALS_JSON, SCOPES)

            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        # Create a DriveService object
        service = build("drive", "v3", credentials=creds)

        # Create a file metadata object. Specifies name of file.
        file_metadata = {"name": part_name}

        # Create a media object. Specifies path to file.
        file_path = f"/Users/owens/music-projects/python-music-utils/test-directory/test-dir1/{part_name}.pdf"  # noqa: E501
        media = MediaFileUpload(file_path)

        # Use the Files().create() method to upload the file
        file = (
            service.files()
            .create(body=file_metadata, media_body=media, fields="id")
            .execute()
        )

        print(f'File ID: {file.get("id")}')

        # ------- original quickstart.py try block - retrieving list of files from user's Drive -------
        # Call the Drive v3 API
        # results = (
        #     service.files()
        #     .list(pageSize=10, fields="nextPageToken, files(id, name)")
        #     .execute()
        # )
        # items = results.get("files", [])

        # if not items:
        #     print("No files found.")
        #     return
        # print("Files:")
        # for item in items:
        #     print(f'{item["name"]} ({item["id"]})')
        #     # print("{0} ({1})".format(item["name"], item["id"]))
        # ------- end original quickstart.py try block -------

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    assert (
        len(argv) == 2
    ), "One argument required for program: python quickstart.py <part_name>"
    # remove '.pdf' extension if user included it
    arg = argv[1]
    part_name = arg[:-4] if arg[-4:] == ".pdf" else arg
    main(part_name)
