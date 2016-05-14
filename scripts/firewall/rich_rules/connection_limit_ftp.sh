#!/bin/bash

#no of connections per minute=$1 $2=add/remove $3=permanent/temporary $4=zone-name (optional)

#on adding --permanent switch rules will be listed after a reboot

#To Add a rule and remove also
if [ $3 = 'permanent' ]
then
firewall-cmd --permanent --zone=$4 --$2-rich-rule="rule service name=ftp limit value=$1/m accept"
firewall-cmd --reload
elif [ $3 = 'temporary' ]
then
firewall-cmd  --zone=$4 --$2-rich-rule="rule service name=ftp limit value=$1/m accept"
else
echo "Invalid argument '$3'"
fi
