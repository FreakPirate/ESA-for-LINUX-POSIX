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