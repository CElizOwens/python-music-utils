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


def auth_to_service():
    creds = None

    # The below is for user (this app) account authentication...
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        # for user (this app) account
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            # for user (this app) account
            # flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            flow = InstalledAppFlow.from_client_config(USER_CREDENTIALS_JSON, SCOPES)

            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        # Create a DriveService object
        service = build("drive", "v3", credentials=creds)
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f"An error occurred while building service: {error}")

    return service


# Creates a child folder in IMSLP folder
def create_IMSLP_subFolder(folder_name):
    service = auth_to_service()
    try:
        # Check that IMSLP folder exists, get id if so
        IMSLP_ID = get_folder_id("IMSLP")
        if not IMSLP_ID:
            IMSLP_ID = create_imslp_folder()
        # Create file folder metadata object, specifying name of folder.
        file_metadata = {
            "name": folder_name,
            "mimeType": "application/vnd.google-apps.folder",
            "parents": [IMSLP_ID],
        }
        folder = service.files().create(body=file_metadata, fields="id").execute()
        print(f'{folder_name} ID: "{folder.get("id")}".')
        print(f"folder = {folder}\n")
        return folder.get("id")

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f"An error occurred while building service: {error}")


def create_lower_folder(parent, new_folder):
    service = auth_to_service()
    try:
        # Check that IMSLP folder exists, get id if so
        PARENT_ID = get_folder_id(parent)
        assert PARENT_ID is not None, f"--> {parent} folder not found.\n"
        # Create file folder metadata object, specifying name of folder.
        file_metadata = {
            "name": new_folder,
            "mimeType": "application/vnd.google-apps.folder",
            "parents": [PARENT_ID],
        }
        folder = service.files().create(body=file_metadata, fields="id").execute()
        print(f'{new_folder} ID: "{folder.get("id")}".')
        print(f"folder = {folder}\n")
        return folder.get("id")

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f"An error occurred while building service: {error}")


def get_folder_id(folder_name):
    service = auth_to_service()
    try:
        results = (
            service.files()
            .list(
                spaces="drive",
                q=f"mimeType='application/vnd.google-apps.folder' and name='{folder_name}'",
                fields="nextPageToken, files(id, name, mimeType)",
            )
            .execute()
        )
        items = results.get("files", [])

        if not items:
            print(f"\n{folder_name} folder does not exist.\n")
            return None

        print(f"\n{folder_name} folder exists:\n -> Results = {items}\n")
        assert len(items) == 1, "More than one IMSLP folder exists."
        print(f'{folder_name} id = {items[0]["id"]}')
        return items[0]["id"]

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f"An error occurred while building service: {error}")

    # def imslpExists():
    service = auth_to_service()
    # Check if IMSLP folder already exists
    try:
        results = (
            service.files()
            .list(
                spaces="drive",
                q="mimeType='application/vnd.google-apps.folder' and name='IMSLP'",
                fields="nextPageToken, files(id, name, mimeType)",
            )
            .execute()
        )
        items = results.get("files", [])

        if not items:
            print("\nIMSLP folder does not exist.\n")
            return False

        print(f"\nIMSLP folder already exists:\n -> Results = {items}\n")
        assert len(items) == 1, "More than one IMSLP folder exists."
        print(f'IMSLP id = {items[0]["id"]}')
        return items[0]["id"]

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f"An error occurred while building service: {error}")


def create_imslp_folder():
    service = auth_to_service()

    try:
        # Create file folder metadata object, specifying name of folder.
        file_metadata = {
            "name": "IMSLP",
            "mimeType": "application/vnd.google-apps.folder",
        }
        file = service.files().create(body=file_metadata, fields="id").execute()
        print(f'Folder ID: "{file.get("id")}".')
        return file.get("id")

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f"An error occurred while building service: {error}")


def upload_part(part_name, folder_id):
    # remove '.pdf' extension if client included it
    part_name = part_name[:-4] if part_name[-4:] == ".pdf" else part_name
    # Run authentication flow and build Drive service
    service = auth_to_service()

    try:
        # Create a file metadata object. Specifies name of file.
        file_metadata = {"name": part_name, "parents": [folder_id]}

        # Create a media object. Specifies path to file.
        file_path = f"/Users/owens/Documents/Opus_Oakland/imslp/Beethoven_Quartet_Op18_No1/{part_name}.pdf"  # noqa: E501
        media = MediaFileUpload(file_path)

        # Use the Files().create() method to upload the file
        file = (
            service.files()
            .create(body=file_metadata, media_body=media, fields="id")
            .execute()
        )

        print(f'File ID: {file.get("id")}')

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f"An error occurred: {error}")


# -------
# listFiles ==> original quickstart.py example
# retrieves list of first ten files from user's Drive
# (only files created by python-music-utils)
# -------


def listFiles():
    """
    Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    try:
        # Run authentication and build Drive service
        service = auth_to_service()
        # Call the Drive v3 API
        results = (
            service.files()
            .list(pageSize=10, fields="nextPageToken, files(id, name, mimeType)")
            .execute()
        )
        items = results.get("files", [])

        if not items:
            print("No files found.")
            return

        print("\nPython Music Utils Resources:")
        for item in items:
            # print(f'File: {item["name"]} | ID: {item["id"]}')
            print(f"File = {item}")
        print("\n")

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    # listFiles()
    # create_imslp_folder()
    # imslpExists()
    # create_subFolder("Beethoven_Op18")
    # get_folder_id("Beethoven_Op18")
    # create_lower_folder("Beethoven_Op18", "Quartet_No1")
    upload_part(
        "breitkopf_beethoven_quartett_op_18_no_1_viola.pdf",
        "1rUq9QVacbO2SKsIC7XOpWGqbnunUQha5",
    )

    # assert (
    #     len(argv) == 2
    # ), "One argument required for part upload: python quickstart.py <part_name>"
    # upload_part(argv[1])
