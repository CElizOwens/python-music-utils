#!usr/bin/env python
import os
from sys import argv
import convert_multiple

# from pathlib import Path
from zipfile import ZipFile

# path to Opus' imslp folder
OPUS_IMSLP = "/Users/owens/Documents/Opus_Oakland/imslp/"
DOWNLOADS = "/Users/owens/Downloads/"

# To run program:
# python process_zipfile.py <path-to-zipfile> <new-folder-name>


def process(zip_name, new_folder):
    # create <new_folder> in OPUS_IMSLP
    new_path = os.path.join(OPUS_IMSLP, new_folder)
    try:
        os.mkdir(new_path)
    except OSError as error:
        print(error)

    zPath = os.path.join(DOWNLOADS, zip_name)
    # mv files from <folder> to <new_folder>
    # opening the zip file in READ mode
    with ZipFile(zPath, "r") as zip:
        # printing all the contents of the zip file
        # zip.printdir()

        # extracting all the files
        print("Extracting all the files now...")
        zip.extractall(new_path)
        print("Done!")

    # convert those files
    convert_multiple.rename_files(new_path)


if __name__ == "__main__":
    assert (
        len(argv) == 3
    ), f"argv = {argv}.\nCorrect format: python process_unzipped_folder.py '<name-of-zipfile in /Downloads>' <new-folder-name>\n"  # noqa: E501
    # call function, passing the two arguments
    process(argv[1], argv[2])
