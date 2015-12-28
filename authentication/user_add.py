"""
User & Password Authentication Module #Insertion#
Responsible for user & password entry

Current: Console based
Scope: GUI implementation
"""

import sys
import hashlib
import getpass
import salt


def user_add(filename):
	# Adds a user name and password pair in the given file
	# It calculates the hash of entered password + generated salt combined

	attempt = 3
	while attempt > 0:
		user_name = raw_input('User Name: ')
		if not salt.exist(user_name, filename):
			break

		attempt = attempt - 1
		print "User already exist: " + str(attempt) + " attempts left\n"

	while True:
		password = getpass.getpass('Enter Password: ')
		re_pass = getpass.getpass('Re-Enter password: ')
		
		if password == re_pass:
			break
		else:
			print "Passwords do not match: Try again!\n\n"

	salt_value = salt.generate(7)			# 7 digit salt value
	hash_val = hashlib.sha224(salt_value + password).hexdigest()		# hash value of salt + entered pass

	stored_pass = salt_value + '$' + hash_val 							# "Salt$Combined_Hash"

	try:
		file_conn = open(filename,'a')									# append new entry
		file_conn.write(user_name + ':')
		file_conn.write(stored_pass + '\n')
		file_conn.close()

	except Exception as e:
		print type(e)
		print e.args
		sys.exit("Problem appending: 'insert()'")

	print '\nPassword safely stored in ' + filename + '\n'


if __name__ == "__main__":
	user_add(sys.argv[1])