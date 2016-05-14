#!/bin/bash

#exposing specified range of ports of a subnet.Will accept,reject ,or drop packets on the specified range of ports

#$1=address of segment( eg:172.168.1.0) $2,$3=port range(start end) $4=protocol-name(tcp,udp) $5=accept/reject/drop
#$6=add/remove $7=permanent $8=zone-name (optional)

#on adding --permanent switch rules will be listed after a reboot

[ -z $7 ] && sudo firewall-cmd    --zone=$8  --$6-rich-rule="rule family=ipv4 source address=$1 port port=$2-$3 protocol=$4 $5" || sudo firewall-cmd --$7   --zone=$8  --$6-rich-rule="rule family=ipv4 source address=$1 port port=$2-$3 protocol=$4 $5"

[ -z $7 ] || sudo firewall-cmd --reload


