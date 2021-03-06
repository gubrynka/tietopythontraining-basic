"""
Program that opens all .txt files in a folder and
searches for any line that matches a user-supplied regular expression.
The results should be printed to the screen.
"""

import re
import os
import argparse
import sys


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Search regex on files')
    parser.add_argument('-p', '--path',
                        help='path to search',
                        default='./')
    parser.add_argument('-r', '--regex',
                        required='True',
                        help='regex to search')
    results = parser.parse_args(args)
    return (results.path,
            results.regex)


def files_in_path(path):
    only_files = [f for f in os.listdir(path)
                  if os.path.isfile(os.path.join(path, f))]
    return only_files


def search_regex(path, regex):
    files = files_in_path(path)
    pattern = re.compile(regex)
    print("Lines contain searched regex:")
    for file_name in files:
        file_with_path = os.path.join(path, file_name)
        file_text = open(file_with_path)
        for line in file_text:
            line = line.rstrip()
            if re.search(pattern, line):
                print(str(file_name) + ": " + str(line))
        file_text.close()
    print("")


def main():
    my_path, my_regex = check_arg(sys.argv[1:])
    search_regex(my_path, my_regex)
    """
    my_path = "./txt_files"
    my_regex = "Ala\d{4}"
    search_regex(my_path, my_regex)
    my_regex = "^@"
    search_regex(my_path, my_regex)
    """


if __name__ == '__main__':
    main()
