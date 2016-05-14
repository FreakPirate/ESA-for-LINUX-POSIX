#!/bin/bash



#$1=ip address  $2=accept/reject/drop $3=add/remove $4=permanent $5=zone-name (optional)

#on adding --permanent switch rules will be listed after a reboot


[ -z $4] && sudo firewall-cmd   --zone=$5  --$3-rich-rule="rule family=ipv4 source address=$1 $2"|| sudo firewall-cmd  --$4  --zone=$5  --$3-rich-rule="rule family=ipv4 source address=$1 $2"

[ -z $4 ] || sudo firewall-cmd --reload


