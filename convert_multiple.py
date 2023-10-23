#!usr/bin/env python
import os

# from sys import argv
import utils.local.create_rename_file as file_namer
import part_name_formatter as formatter


# pass in directory with multiple IMSLP files
def rename_files(directory):
    # change to the directory
    os.chdir(directory)
    # get array of files
    filenames = os.listdir()
    # loop through files
    for filename in filenames:
        # pass file name into formatter and store result
        formatted = formatter.convert(filename)
        # pass file name and result into file_namer (Success or failure will be logged)
        file_namer.rename_file(filename, formatted, directory)

    print(f"New file names:\n{os.listdir()}")


if __name__ == "__main__":
    rename_files(
        "/Users/owens/Documents/OCO_parts/23-24/Set_2/Turina_Danza-fantàsticas"
    )
