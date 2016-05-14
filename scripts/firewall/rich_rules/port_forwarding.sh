#!/bin/bash

#port forwarding to same pc as well as to different pc as well

#ip =$1.  source port=$2. protocol-name(tcp,udp)=$3.  destination-port=$4. $7=another pc's ip (optional). add/remove=$5/.  1.(permanent)/2.(temperory)=$6

#on adding --permanent switch, rules will be listed after a reboot/reload of service


if [ $6 = 'temporary' ]  
then
echo "if"
[ -z $7 ] && sudo firewall-cmd   --$5-rich-rule "rule family=ipv4 source address=$1 forward-port port=$2 protocol=$3 to-port=$4" || sudo firewall-cmd    --$5-rich-rule "rule family=ipv4 source address=$1 forward-port port=$2 protocol=$3 to-port=$4 to-addr=$7"

else
echo "else"
[ -z $7 ] && sudo firewall-cmd  --permanent  --$5-rich-rule "rule family=ipv4 source address=$1 forward-port port=$2 protocol=$3 to-port=$4" || sudo firewall-cmd  --permanent  --$5-rich-rule "rule family=ipv4 source address=$1 forward-port port=$2 protocol=$3 to-port=$4 to-addr=$7"
sudo firewall-cmd --reload
fi


