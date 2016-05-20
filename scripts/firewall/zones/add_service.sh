#!/bin/bash

#add a source in a specified zone name


firewall-cmd --zone=$2 --add-service=$1

