#!/bin/bash

# $1= u/g/o (user,group,other ) ; $2=name of user/group/ ('null' for others);  $3=filepath/directorypath (absolute path) ;

# $4 = yes/no (for default acl -- only for directories)


if [ $1 = u ]
then

[ $4 = yes ] && sudo setfacl -x d:$1:$2  $3 || sudo setfacl -x $1:$2  $3 

elif [ $1 = g ]
then
 
[ $4 = yes ] && sudo setfacl -x d:$1:$2  $3 || sudo setfacl -x $1:$2 $3

else

[ $4 = yes ] && sudo setfacl -m d:$1:r  $3 ||sudo setfacl -m $1:r $3 #[ $2 set to be null in this case ]
 
fi 



