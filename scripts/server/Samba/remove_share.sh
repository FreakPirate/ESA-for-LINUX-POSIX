#!/bin/bash

# $1 = name-of-share

sudo sed -i "/$1/,+6d" /etc/samba/smb.conf
