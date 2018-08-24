'''
Verbose output - add configurable logger and 'verbose output'
command line argument to project 1 from lesson 11 to allow
the user to follow intermediate steps of program execution.
The program must allow to configure verbosity on at least 3
levels - disabled, warning (warns and errors only) and info
(most detailed)

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
import logging


def check_arg(args=None):
    parser = argparse.ArgumentParser(
        description='Search all .txt files for user specified \
        regular expression')
    parser.add_argument('-r', '--regex',
                        help='regular expression',
                        required='True',
                        default='')
    parser.add_argument('-d', '--dir',
                        help='path to txt. files',
                        default='.')
    parser.add_argument('-v', '--verbose',
                        help='verbosity level: off|warn|info',
                        choices=('off', 'warn', 'info'),
                        default='off')

    results = parser.parse_args(args)
    return(results.regex,
           results.dir,
           results.verbose)


def regex_search():
    search_rule, path_to_files, verbose = check_arg(sys.argv[1:])
    if verbose == 'off':
        # disable all levels
        logging.disable(logging.CRITICAL)
    elif verbose == 'warn':
        # disable DEBUG and INFO level
        # enabled will be only  WARNING, ERROR, CRITICAL levels
        logging.disable(logging.INFO)
    try:
        for file_name in os.listdir(path_to_files):
            try:
                if file_name.endswith(".txt"):
                    print("Searching file: ", file_name)
                    logging.info("Searching file: " + file_name)
                    text_file = open(file_name)
                    content = text_file.read()
                    regex_rule = re.compile(search_rule)
                    res = regex_rule.findall(content)
                    print(res)
            except FileNotFoundError as e:
                print("FileNotFoundError: " + str(e))
                logging.error("File not found" + str(e))
    except PermissionError:
        print("PermissionError")
        logging.error("Permission error")


if __name__ == "__main__":
    # default enalbe all levels of logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s- %(levelname)s - %(message)s')
    regex_search()
