#!usr/bin/env python
import os
from sys import argv
import utils.local.create_rename_file as file_namer
import part_name_formatter as formatter


# pass in directory with multiple IMSLP files
def rename_file(file, directory):
    # change to the directory
    os.chdir(directory)
    # pass file into formatter and store result
    formatted = formatter.convert(file)
    # pass file and result into file_namer (Success or failure will be logged)
    file_namer.rename_file(file, formatted, directory)

    print(f"File names:\n{os.listdir()}")


if __name__ == "__main__":
    print(f"---> argv = {argv}")
    assert len(argv) == 2, "Must provide two arguments: file directory"
    file, directory = argv[0], argv[1]
    rename_file(file, directory)
