#!usr/bin/env python
import os
from sys import argv


APP_DIR = "/Users/owens/music-projects/python-music-utils/test-directory/test-dir1/"


# creates new files in APP_DIR or finds existingfile in APP_DIR and renames it
# args array: create_file.py newfilename | existingfilename newfilename
def create_file(args):
    assert (
        len(args) > 1
    ), "Must provide at least one argument: newfilename | existingfilename newfilename"
    # append new or existing filename to APP_DIR (APP_DIR/filename)
    file_path = APP_DIR + args[1]
    # if existing filename and new filename given, rename file
    if len(args) == 3:
        renamed_file_path = APP_DIR + args[2]
        os.rename(file_path, renamed_file_path)
        print(f"\nSuccess! File renamed:\n{renamed_file_path}\n")
    else:
        with open(file_path, "x") as my_file:
            my_file.write("File created by create-rename_file.py")
        # open(file_path, "x").close()
        print(f"\nSuccess! File created:\n{file_path}\n")


create_file(argv)
