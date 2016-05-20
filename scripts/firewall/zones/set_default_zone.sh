#!/bin/bash

#set default zone of user

read name
firewall-cmd --set-default-zone=$name

