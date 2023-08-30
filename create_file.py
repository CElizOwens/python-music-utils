#!usr/bin/env python
import os
from sys import argv


TEST_DIR = "/Users/owens/music-projects/test-directory/python-music-utils/"


# args array: create_file.py newfile | currfile[ newfilename]
def create_file(args):
    assert len(args) > 1, "Must provide one argument: new-file-name"
    new_file = TEST_DIR + args[1]
    if len(args) == 3:
        # rename given file
        os.rename(new_file, TEST_DIR + args[2])
        print("\nSuccess!\nRenamed file.\n")
    else:
        open(new_file, "w").close()
        print(f"\nSuccess!\nCreated file {new_file}\n")


create_file(argv)
