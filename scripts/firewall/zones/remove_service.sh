#!/bin/bash

#add a source in a specified zone name


firewall-cmd --zone=$2 --remove-service=$1

