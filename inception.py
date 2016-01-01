"""
Core functional and management module for the whole project
"""

import sys
from auth import user_auth, user_add

def main(args = 'passwd.lck'):

    filename = args

    print "\n\nEnhanced Security Agent (ESA) for POSIX systems (v1.0, console based)\n\n"
    while True:
        print "Choose from either:"
        print "1. Add a new entry"
        print "2. Authenticate"
        print "0. Exit\n"

        val = int(raw_input('Choice: '))

        if val is 1:
            user_add.add(filename)
        elif val is 2:
            user_auth.auth(filename)
        elif val is 0:
            break
        else:
            print "Invalid input: Try again!"

    print "\nThanks for using ESA!\nTerminating..."

if __name__ == '__main__':
    main()
