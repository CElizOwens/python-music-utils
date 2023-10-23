#!usr/bin/env python
import os

# from sys import argv


# APP_DIR = "/Users/owens/music-projects/python-music-utils/test-directory/test-dir1/"
# DIR = "/Users/owens/Documents/OCO_parts/23-24/Set_2/Turina_Danza-fantàsticas/"


# creates new files in DIR or finds existingfile in DIR and renames it newfilename
# args array: create_file.py newfilename | existingfilename newfilename
def create_file(new_file, directory):
    assert new_file, "Must provide two arguments: newfilename, directory"
    DIR = directory
    # append new filename to DIR (DIR + "/" + filename)
    file_path = f"{DIR}/{new_file}"

    with open(file_path, "x") as my_file:
        my_file.write("File created by create_rename_file.py")
    # open(file_path, "x").close()
    print(f"\nSuccess! File created:\n{file_path}\n")


def rename_file(curr_name, new_name, directory):
    assert (
        curr_name and new_name
    ), "Must provide three arguments: currentfilename newfilename directory"
    DIR = directory
    # append existing filename to DIR (DIR + "/" + filename)
    file_path = f"{DIR}/{curr_name}"
    # rename file
    renamed_file_path = f"{DIR}/{new_name}"
    os.rename(file_path, renamed_file_path)
    print(f"\nSuccess! File renamed:\n{renamed_file_path}\n")


# create_file(argv)
