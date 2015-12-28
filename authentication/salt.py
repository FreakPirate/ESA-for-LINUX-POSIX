import string
import random
import os.path
import sys

def generate(size=6, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
	saltStr = ''.join(random.choice(chars) for i in range(size))
	
	return saltStr


def exist(user, file_):
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
