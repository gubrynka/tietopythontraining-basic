'''
Selective Copy
Write a program that walks through a folder tree
and searches for files with a certain file extension
(such as .pdf or .jpg).
Copy these files from whatever
location they are in to a new folder.
'''
# ! python3
# selective_copy.py - copies files with selected extension
# to the new folder
import os
import shutil


def selective_copy(extension, folder_to_walk, out_folder):
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)
    for folder_name, sub_folders, file_names in os.walk(folder_to_walk):
        for file_name in file_names:
            if file_name.endswith(extension):
                source_path = os.path.abspath(
                    os.path.join(folder_name, file_name))
                destination_path = os.path.abspath(out_folder)
                if os.path.abspath(out_folder) != os.path.abspath(folder_name):
                    print("Copying file: ", file_name)
                    # print("Source: ", source_path)
                    # print("Destination: ", destination_path)
                    shutil.copy(source_path, destination_path)


if __name__ == "__main__":
    selective_copy(".py", ".", "out_folder")
