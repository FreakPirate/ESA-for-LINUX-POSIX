#!/bin/bash

# $1 = workgroup-name ; $2 = netbios-name

sudo sed -i "89c \	workgroup = $1" /etc/samba/smb.conf

sudo sed -i "92c  \	netbios name = $2" /etc/samba/smb.conf



