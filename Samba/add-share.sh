#!/bin/bash

#  $1=Name of share ;  $2=shared-path;  $3=yes/no (for browseable) ; $4=yes/no (for writeable) ;

#  $5=yes/no (for printable); $6=yes/no (for enabling guest-ok) ; $7=comment ; $8=usernames (for valid users)

sudo sed -i "/homes/i [$1]" /etc/samba/smb.conf

sudo sed -i "/homes/i \	comment = [$7]" /etc/samba/smb.conf

sudo sed -i "/homes/i \	path = $2" /etc/samba/smb.conf

sudo sed -i "/homes/i \	browseable = $3" /etc/samba/smb.conf

sudo sed -i "/homes/i \	writeable = $4" /etc/samba/smb.conf

sudo sed -i "/homes/i \	printable = $5" /etc/samba/smb.conf

sudo sed -i "/homes/i \	guest ok = $6" /etc/samba/smb.conf

[ -z $8 ] || sudo sed -i "/homes/i \	valid users = $8" /etc/samba/smb.conf





