#!/bin/bash

#$1=username ; $2=password ; $3=ipaddress-of-remote-machine ; $4=directory-to-mount ; $5=mount-point-name

sudo mkdir $5 2>/dev/null
sudo touch /credentials
sudo echo -e "username=$1\npassword=$2 ">> /credentials 
cat /credentials
sudo mount -t cifs -o username=$1 //$3/$4  $5 
