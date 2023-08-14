#!usr/bin/python3

"""
Command line: python3 create_single_dir.py directory_name [parent_path]
- parent_path: full path of target parent directory
- adds trailing slash to parent_path if not included
- creates a new directory 'path/to/directory_name'
- Defaults to 'Users/owens/music-projects/directory_name when no parent_path
- Note: os.mkdir creates directory in present working directory by default
"""
import os
from sys import argv

DEFAULT_PATH = "/Users/owens/music-projects/python-music-utils/"


def create_directory(args):
    print(args)
    assert (
        len(args) > 1
    ), "Must pass one to two arguments: 'directory_name [parent_path]'"

    directory_name = args[1]
    full_path = ""

    if len(args) >= 3:
        # adds trailing forward slash if not provided by client
        parent_path = args[2] if args[2][-1] == "/" else args[2] + "/"
        full_path = f"{parent_path}{directory_name}"
    else:
        full_path = f"{DEFAULT_PATH}{directory_name}"

    # print("Listing dir: ", os.listdir())
    try:
        os.mkdir(full_path)
        success(full_path)
    except OSError as error:
        print(error)


def success(directory):
    print(f"\nDirectory '{directory}' created.\n")


create_directory(argv)
