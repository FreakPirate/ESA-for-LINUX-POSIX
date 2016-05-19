#!/bin/bash

# $1= u/g/o (user,group,other ) ; $2=name of user/group;  $3=permissions(rwx,rw,rx,etc) ; $4=filepath/directorypath (absolute path) ;

# $5 = yes/no ( set recursively --only for directories )


if [ $1 = u ]
then

[ $5 = yes ] && setfacl -R -m d:$1:$2:$3 $4 || setfacl -m d:$1:$2:$3 $4

elif [ $1 = g ]
then
 
[ $5 = yes ] && setfacl -R -m d:$1:$2:$3 $4 || setfacl -m d:$1:$2:$3 $4

else

[ $5 = yes ] && setfacl -R -m d:$1:$3 $4 || setfacl -m d:$1:$3 $4 #( name of user set to be null in this case )
 
fi 



