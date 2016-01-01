"""
User & Password Authentication Module #Auth#
Responsible for user validation

Current: Console based
Scope: GUI implementation
"""

import sys
import hashlib
import getpass


def process_file(file_):

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


def auth(filename):
    try:
        pass_try = 0
        pass_allowed = 3		#Incorrect password allowed

        auth_flag = 0			# check user validation

        cal_hash_val = ''		# calculated hash value from user entered password
        stored_pass = ''		# stored password as "Salt + Hash"
        hash_val = ''			# separated hash value
        salt_val = ''			# separated/referenced hash value
        hash_list = []			# list to separate salt from total salt value

        user_names, passwords = process_file(filename)		# list of UserNames and Passwords

        user = raw_input('User Name: ')

        # Invalid user name
        if not user in user_names:
            sys.exit('Authentication failed: user ' + user + ' does not exist\nTerminating!')

        # user respective password
        stored_pass = passwords[user_names.index(user)].split('\n')[0]

        #print repr(stored_pass)

        hash_list = stored_pass.split('$')
        salt_val = hash_list[0]
        hash_val = hash_list[1]

        while pass_try < pass_allowed:
            user_pass = getpass.getpass('Enter Password: ')

            # Calculation of hash value based on entered password
            cal_hash_val = hashlib.sha224(salt_val + user_pass).hexdigest()

            # Comparison of stored and calculated hash value for authentication
            if cal_hash_val != hash_val:
                pass_allowed -= 1
                print "Incorrect password: " + str(pass_allowed) + " more attempts left\n"
            else:
                auth_flag = 1
                break

        if auth_flag == 0:
            print "Authentication failed: Terminating\n\n"
        else:
            print "User logged in successfully!\n\n"

    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst

if __name__ == "__main__":
    filename = 'passwd.lck'
    auth(filename)