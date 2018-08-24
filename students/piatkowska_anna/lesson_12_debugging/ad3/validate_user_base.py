'''
Validated user base - write script that takes email, password,
phone number and postal code, validates these fields and if
validation passes, saves it to a file as CSV with email considered
as unique field. If a record with the same email is already in the file,
the old record should be altered by new one.
Use validators implemented in lesson 8, exercises 2, 3, 4 and 5.
As part of this exercise write combined_validator function that
takes email, password, phone number and postal code and throws
exceptions if any of arguments doesn't pass validation. Add 'verbose output'.
'''


# ! python3
# validate_user_base.py -
#
# Usage: py.exe validate_user_base.py <regular_expresion> <dir_path>
#   <regular_expresion> - specifies regular expression,
#   <dir_path>          - path to txt. files if not specified then
#                         current dir are searched


import sys
import argparse
import logging
import email_validator
import strong_password_detection as spd
import phone_number_validator as pnv
import postal_code_validator as pcv
import os


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Script that takes email,\
    password, phone number and postal code,\
    validates these fields and if validation passes, saves it to a file\
    as CSV with email considered as unique field.')
    parser.add_argument('-e', '--email',
                        help='email address',
                        required='True',
                        default='')
    parser.add_argument('-p', '--password',
                        help='password',
                        default='')
    parser.add_argument('-pn', '--phonenumber',
                        help='phone number',
                        default='')
    parser.add_argument('-pc', '--postalcode',
                        help='postal code',
                        default='')
    parser.add_argument('-v', '--verbose',
                        help='verbosity level: off|warn|info',
                        choices=('off', 'warn', 'info'),
                        default='off')

    results = parser.parse_args(args)
    return(results.email,
           results.password,
           results.phonenumber,
           results.postalcode,
           results.verbose)


def validate_user():
    email, password, phone_number, postal_code, verbose = check_arg(
        sys.argv[1:])
    if verbose == 'off':
        logging.disable(logging.CRITICAL)
    elif verbose == 'warn':
        logging.disable(logging.INFO)
    try:
        combined_validator(email, password, phone_number, postal_code)
    except Exception as err:
        logging.error("Validation error:" + str(err))
        return
    store_record(email, password, phone_number, postal_code)


def combined_validator(email, password, phone_number, postal_code):
    if not email_validator.validate_email(email):
        raise Exception("email validation failed: " + email)
    else:
        logging.info("email valid " + email)
    if not spd.is_it_strong_password(password):
        raise Exception("password validation failed: " + password)
    else:
        logging.info("password valid " + password)
    if not pnv.validate_number(phone_number):
        raise Exception("Phone number validation failed: " + phone_number)
    else:
        logging.info("Phone number valid " + phone_number)
    if not pcv.validate_postal_code(postal_code):
        raise Exception("Postal code not valid: " + postal_code)
    else:
        logging.info("Postal code valid " + postal_code)


def store_record(email, password, phone_number, postal_code):
    rows = []
    if os.path.exists("data_base.csv"):
        logging.info("Data base file already exists.")
        data_base = open("data_base.csv", "r")
        rows = data_base.readlines()
        data_base.close()
    data_base = open("data_base.csv", "w")
    was_in_db = False
    for row in rows:
        db_email, db_password, db_phone_number, db_postal_code = row.split(';')
        if db_email == email:
            logging.info("Email already exists in data base.")
            data_base.write(
                ';'.join([email, password, phone_number, postal_code]))
            data_base.write('\n')
            was_in_db = True
        else:
            data_base.write(row)
    if not was_in_db:
        logging.info("New email added to data base.")
        data_base.write(';'.join([email, password, phone_number, postal_code]))
        data_base.write('\n')


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s- %(levelname)s - %(message)s')
    validate_user()
