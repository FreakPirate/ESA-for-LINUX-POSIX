#!/bin/bash

#list all the rich rules in the specified zone

firewall-cmd --list-rich-rules  --zone=$1
