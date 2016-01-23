"""
User & Password Authentication Module #Auth#
Responsible for user validation

Current: Console based
Scope: GUI implementation
"""

import os.path
import hashlib
from salt import process_passwd_file


def check(username, password, filename='passwd.lck'):
    try:
        if not os.path.isfile(filename):
            return False

        user_list, pass_list = process_passwd_file(filename)  # list of UserNames and Passwords

        # Invalid user name
        if not username in user_list:
            return False

        # user respective password
        stored_pass = pass_list[user_list.index(username)].split('\n')[0]

        # print repr(stored_pass)

        hash_list = stored_pass.split('$')  # list of extracted salt + pass
        salt_val = hash_list[0]  # extracted salt value
        hash_val = hash_list[1]  # extracted Hash value

        cal_hash_val = hashlib.sha224(salt_val + password).hexdigest()

        # Comparison of stored and calculated hash value for authentication
        if cal_hash_val != hash_val:
            return False
        else:
            return True

    except Exception as inst:
        print type(inst)  # the exception instance
        print inst.args  # arguments stored in .args
        print inst


if __name__ == "__main__":
    filename = 'passwd.lck'
    print check('freak', 'freak', filename)
