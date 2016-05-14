#!/bin/bash

#$1=source-ip-address $2=zone-name (optional)


firewall-cmd --zone=$2 --remove-source=$1

