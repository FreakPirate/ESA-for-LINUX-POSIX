"""
User & Password Authentication Module #Insertion#
Responsible for user & password entry

Current: Console based
Scope: GUI implementation
"""
import hashlib
import salt
import os.path

def add(username, email, phone, password, sec_ques, sec_ans, file_pass='passwd.lck', file_shadow='shadow.lck'):
    # Adds a user name and password pair in the given file
    # It calculates the hash of entered password + generated salt combined
    user_list = []
    email_list = []
    pass_list = []
    phone_list = []

    if os.path.isfile(file_pass):
        user_list, pass_list = salt.process_passwd_file(file_pass)

    if os.path.isfile(file_shadow):
        email_list, phone_list = salt.process_shadow_file(file_shadow)

    if username in user_list:
        return "username"
    elif email in email_list:
        return "email"
    elif phone in phone_list:
        return "phone"

    salt_val = salt.generate()
    hash_val = salt_val + '$' + hashlib.sha224(salt_val + password).hexdigest()

    try:
        file_conn_p = open(file_pass, 'a')
        file_conn_s = open(file_shadow, 'a')

        passwd_str = username + ':' + hash_val + '\n'
        shadow_str = email + ':' + phone + ':' + sec_ques + ':' + sec_ans + '\n'

        file_conn_p.write(passwd_str)
        file_conn_s.write(shadow_str)

        file_conn_p.close()
        file_conn_s.close()

        return "accept"

    except Exception as e:
        return "reject"
        print type(e)
        print e.args


if __name__ == "__main__":
    username = raw_input('username> ')
    password = raw_input('password> ')
    email = raw_input('email> ')
    phone = raw_input('phone> ')
    sec_ques = raw_input('security question> ')
    sec_ans = raw_input('security answer> ')

    file_pass = 'passwd.lck'
    file_shadow = 'shadow.lck'
    add(username, email, phone, password, sec_ques, sec_ans, file_pass, file_shadow)
