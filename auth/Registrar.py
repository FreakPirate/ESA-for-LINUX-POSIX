"""
User & Password Authentication Module #Insertion#
Responsible for user & password entry

Current: Console based
Scope: GUI implementation
"""
import hashlib
import salt
import sqlite3 as sqlite
import helper.FetchDB as fetch

def add(username, email, phone, password, sec_ques, sec_ans, database="./database/user.sqlite", table_names=["passwd", "shadow"]):
    # Adds a user name and password pair in the given file
    # It calculates the hash of entered password + generated salt combined

    ATTR_USER_NAME = "Name"
    ATTR_EMAIL_ID = "EmailId"

    user_list = fetch.getColumnList(ATTR_USER_NAME, database, table_names[0])
    email_list = fetch.getColumnList(ATTR_EMAIL_ID, database, table_names[1])


    if username in user_list:
        return "username"
    elif email in email_list:
        return "email"

    salt_val = salt.generate()
    hash_val = salt_val + '$' + hashlib.sha224(salt_val + password).hexdigest()

    conn = None

    try:
        conn = sqlite.connect(database)
        cur = conn.cursor()

        query = "INSERT"
        cur.execute


    except lite.Error, e:
        print "Error %s:" % e.args[0]
        if conn:
            conn.close()
        return "reject"

    finally:
        if conn:
            conn.close()


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
