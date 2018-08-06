'''
Write a program that opens all .txt files in a folder
and searches for any line that matches a user-supplied
regular expression. The results should be printed to the screen.
'''
# ! python3
# regex_search.py - search all .txt files
# for user specified regular expression
# Usage: py.exe regex_search.py <regular_expresion> <dir_path>
#   <regular_expresion> - specifies regular expression,
#   <dir_path>          - path to txt. files if not specified then
#                         current dir are searched

import sys
import os
import re
import argparse


def check_arg(args=None):
    parser = argparse.ArgumentParser(description=
    'Search all .txt files for user specified regular expression')
    parser.add_argument('-r', '--regex',
                        help='regular expression',
                        required='True',
                        default='')
    parser.add_argument('-d', '--dir',
                        help='path to txt. files',
                        default='.')
    
    results = parser.parse_args(args)
    return(results.regex,
           results.dir)


def regex_search():
    search_rule, path_to_files = check_arg(sys.argv[1:])
    try:
        for file_name in os.listdir(path_to_files):
            try:
                if file_name.endswith(".txt"):
                    print("Searching file: ", file_name)
                    text_file = open(file_name)
                    content = text_file.read()
                    regex_rule = re.compile(search_rule)
                    res = regex_rule.findall(content)
                    print(res)
            except FileNotFoundError as e:
                print("FileNotFoundError: " + str(e))
    except PermissionError:
        print("PermissionError")


if __name__ == "__main__":
    regex_search()
