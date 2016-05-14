#!/bin/bash

# Masquerade a source ip address


#$1=source ip address  $2=add/remove $3=permanent (optional)
[ -z $3 ] && sudo firewall-cmd   --$2-rich-rule="rule family=ipv4 source address=$1  masquerade"  || sudo firewall-cmd  --$3 --$2-rich-rule="rule family=ipv4 source address=$1  masquerade" 

[ -z $3 ] || sudo firewall-cmd --reload
