"""
User & Pass Authenctication module #Salt

This module is responsible for Salt generation
and checking occurence of User Names in authentication file
"""

import string
import random
import os.path
import sys


def generate(size=6, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    # generate a salt (random alphanumeric value) of given size and character choice
    salt_str = ''.join(random.choice(chars) for i in range(size))

    return salt_str


def exist(user, file_):
    # Check whether the entered user_name exists in the authentication file or not
    if not os.path.isfile(file_):
        return False

    try:
        file_conn = open(file_, 'r')

        for line in file_conn:
            reg_user = line.split(':')[0]

            if user == reg_user:
                return True

        file_conn.close
        return False
    except:
        sys.exit("Problem handling file: 'exist()'")


def existInLine(user, line_):
    reg_user = line_.split(':')[0]

    if user == reg_user:
        return True
    else:
        return False


def process_passwd_file(file_):

    # Function is dedicated to separate user_names and passwords in the form of list
    user_names = []
    passwords = []

    try:
        file_conn = open(file_, 'r')

        for line in file_conn:
            temp = line.split(':')
            user_names.append(temp[0])
            passwords.append(temp[1])

        file_conn.close()
        return user_names , passwords

    except Exception as e:
        print type(e)
        print e.args


def process_shadow_file(file_):
    email = []
    phone = []
    sec_ques = []
    sec_ans = []

    try:
        file_conn = open(file_, 'r')

        for line in file_conn:
            temp = line.split(':')
            email.append(temp[1])
            phone.append(temp[2])
            # sec_ques.append(temp[3])
            # sec_ans.append(temp[4])

        file_conn.close()

        return email, phone

    except Exception as e:
        print type(e)
        print e.args