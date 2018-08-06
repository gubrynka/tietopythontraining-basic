'''
Filling in the Gaps
Write a program that finds all files with a given prefix,
such as spam001.txt, spam002.txt, and so on, in a single
folder and locates any gaps in the numbering
(such as if there is a spam001.txt and spam003.txt but no spam002.txt).
Have the program rename all the later files to close this gap.

As an added challenge, write another program that
can insert gaps into numbered files so that a new file can be added.
'''
import os
import shutil
import random
import sys
import argparse


def check_arg(args=None):
    parser = argparse.ArgumentParser(description=
        "Finds all files with a given prefix in a given\
         folder and locates any gaps in the numbering e.g.\
         gap is when there is a spam001.txt and spam003.txt\
         but no spam002.txt\
         Program can close such gap or when there is no gap\
         insert the gap.")
    parser.add_argument('-s', '--switch',
                        metavar = 'c|i',
                        choices = ['c', 'i'],
                        help='c-close the gap, i-insert the gap',
                        default='c')
    parser.add_argument('-e', '--extension',
                        metavar = '<extension>',
                        help='file extension e.g \".txt\"',
                        # required='True',
                        default='.txt')
    parser.add_argument('-d', '--dir',
                        metavar = '<dir_name>',
                        help='directory where file will be searched',
                        default='.\\ad3')
    parser.add_argument('-p', '--prefix',
                        metavar = '<file_prefix>',
                        help='file prefix',
                        default='spam')

    results = parser.parse_args(args)
    return(results.switch,
           results.dir,
           results.prefix,
           results.extension)


def find_files(folder_name, file_prefix, file_extension):
    file_list = []
    if os.path.exists(folder_name):
        for file in os.listdir(folder_name):
            if file.startswith(file_prefix) and file.endswith(file_extension):
                file_list.append(file)
        file_list.sort()
        return file_list
    else:
        print("Directory not found:", folder_name)
        return []


def close_the_gap(folder_name, file_prefix, file_extension):
    print("Closing the gap...")
    file_list = find_files(folder_name, file_prefix, file_extension)
    if len(file_list) == 0:
        return
    numbers_size = 3
    if len(file_list) > 999:
        numbers_size = int(len('%d' % len(file_list)))
    last_file_name = '%s%0*d%s' % (file_prefix,
                                   numbers_size, len(file_list),
                                   file_extension)
    if last_file_name == file_list[-1]:
        print("The gap is closed already.")
    else:
        for file_number in range(1, len(file_list) + 1):
            new_file_name = '%s%0*d%s' % (file_prefix,
                                          numbers_size, file_number,
                                          file_extension)
            new_file_abs_path = os.path.abspath(
                os.path.join(folder_name, new_file_name))
            old_file_abs_path = os.path.abspath(
                os.path.join(folder_name, file_list[file_number - 1]))
            if old_file_abs_path != new_file_abs_path:
                print("Old:", old_file_abs_path)
                print("New:", new_file_abs_path)
                shutil.move(old_file_abs_path, new_file_abs_path)


def insert_the_gap(folder_name, file_prefix, file_extension):
    print("Inserting a gap...")
    file_list = find_files(folder_name, file_prefix, file_extension)
    if len(file_list) == 0:
        return
    file_number = len(file_list)
    numbers_size = 3
    if len(file_list) > 999:
        numbers_size = int(len('%d' % len(file_list)))
    last_file_name = '%s%0*d%s' % (file_prefix,
                                   numbers_size, file_number, file_extension)
    if last_file_name != file_list[-1]:
        print("The gap is already there.")
    else:
        gap_number = random.randint(1, len(file_list))
        for number in range(len(file_list) + 1, gap_number, -1):
            old_file_abs_path = os.path.abspath(
                os.path.join(folder_name, file_list[number - 2]))
            new_file_name = '%s%0*d%s' % (file_prefix,
                                          numbers_size, number, file_extension)
            new_file_abs_path = os.path.abspath(
                os.path.join(folder_name, new_file_name))
            print('Old:', old_file_abs_path)
            print('New', new_file_abs_path)
            shutil.move(old_file_abs_path, new_file_abs_path)


if __name__ == "__main__":
    switch, dir, file_prefix, extension = check_arg(sys.argv[1:])
    if switch == 'c':
        close_the_gap(dir, file_prefix, extension)
    elif switch == 'i':
        insert_the_gap(dir, file_prefix, extension)
