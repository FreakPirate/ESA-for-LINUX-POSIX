#!/bin/bash

#  $1=Name of share ;  $2=shared-path;  $3=yes/no (for browseable) ; $4=yes/no (for writeable) ;

#  $5=yes/no (for printable); $6=yes/no (for enabling guest sharing without password) ; $7=comment ; 

#  $8  = samba-username/n (for valid users/guest ) ; $9=samba-password of user/n (null in case of guest sharing) 

sudo sed -i "/homes/i [$1]" /etc/samba/smb.conf

sudo sed -i "/homes/i \	comment = $7" /etc/samba/smb.conf

sudo sed -i "/homes/i \	path = $2" /etc/samba/smb.conf

sudo sed -i "/homes/i \	browseable = $3" /etc/samba/smb.conf

sudo sed -i "/homes/i \	writeable = $4" /etc/samba/smb.conf

sudo sed -i "/homes/i \	printable = $5" /etc/samba/smb.conf

sudo sed -i "/homes/i \	guest ok = $6" /etc/samba/smb.conf


sudo systemctl restart smb.service
sudo systemctl restart nmb.service

if [ $6 = 'yes' ] 
then

sudo chmod -R 0755 $2
sudo chown -R nobody:nobody $2
sudo chcon -t samba_share_t $2

else 

sudo sed -i "/homes/i \ valid users = @smbgrp "
sudo useradd $8 -G smbgrp 2> /dev/null
echo $9 | sudo passwd --stdin $8 
sudo chmod -R 0777 $2
sudo chcon -t samba_share_t $2
fi













