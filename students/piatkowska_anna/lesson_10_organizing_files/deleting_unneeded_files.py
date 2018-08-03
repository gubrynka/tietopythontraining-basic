'''
Deleting Unneeded Files
It’s not uncommon for a few unneeded but humongous files
or folders to take up the bulk of the space on your hard drive.
If you’re trying to free up room on your computer,
you’ll get the most bang for your buck by deleting
the most massive of the unwanted files.
But first you have to find them.

Write a program that walks through a folder
tree and searches for exceptionally large files or folders—say,
ones that have a file size of more than 100MB.
(Remember, to get a file’s size, you can use os.path.getsize()
from the os module.)
Print these files with their absolute path to the screen.
'''


import os


def find_large_files_and_folders(folder_to_search):
    print("Searching for files and folder with size above 100 MB in",
          folder_to_search)
    for folder_name, sub_folders, file_names in os.walk(folder_to_search):
        folder_size = 0
        for file_name in file_names:
            file_size = os.path.getsize(os.path.abspath(
                os.path.join(folder_name, file_name)))
            folder_size += file_size
            if file_size > 100000000:
                print(os.path.abspath(os.path.join(folder_name, file_name)))
        if folder_size > 100000000:
            print(os.path.abspath(folder_name))


if __name__ == "__main__":
    find_large_files_and_folders("c:\\windows")
