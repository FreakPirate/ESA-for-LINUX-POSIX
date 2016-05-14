#!/bin/bash

echo "********************Hello User*****************"
echo "-------------------------------"
echo "This Step Would Help You Set Up Access Control List on Named Users, On Named Group as well as on Other Users also"
echo "-------------------------------"

while :
do
echo "-------------------------------"
echo "Your Choices"
echo "-------------------------------"
echo "1.  Get An Access Control List"
echo "2.  Set An Access Control List"
echo "3.  Exit "
echo "-------------------------------"
read -p "enter your choice " ch1


if	[ $ch1 -eq 1 ] 
then
echo "-------------------------------"
read -p "Enter FileName Or its Absolute Path  " ch2


getfacl $ch2
read -p "Press [Enter] key to continue..."
readEnterKey  

elif	[ $ch1 -eq 2 ] 
then
echo "-------------------------------"
echo "1.  Set from already existing file"
echo "2.  Set new controls"
echo "-------------------------------"
read -p " Your choice " ch3

      if [ $ch3 -eq 1 ] 
      then
      read -p "Enter Source File Name Or Path " s_path 
      read -p "Enter Destination File Name Or Path " d_path
      getfacl $s_path| setfacl --set-file=- $d_path
      read -p "Press [Enter] key to continue..."
readEnterKey

      elif [ $ch3 -eq 2 ]
      then
      echo "-------------------------------" 
      read -p "Enter File Name Or Path  " f_path
      echo "-------------------------------"
      echo " 1. Restrict a Named User "
      echo " 2. Restrict a Named Group "
      echo " 3. Restrict Other Users "
      echo "-------------------------------"
      read -p " Enter Your Choice " ch4
      echo "-------------------------------"
      echo "( 'r' - read )"
      echo "( 'w' - write )"
      echo "( 'x' - execute)"
      echo "( '-' - null permissions)"

      echo "(***Note:combine in the same order******)"
      case $ch4 in
      "1")
          echo "-------------------------------"
          read -p "Enter Username and Permissions (seperated by space) " name perm 
          setfacl -m u:$name:$perm $f_path
          read -p "Press [Enter] key to continue..."
readEnterKey;;
      "2")echo "-------------------------------"
          read -p "Enter Groupname and Permissions (seperated by space) " name perm 
          setfacl -m g:$name:$perm $f_path
          read -p "Press [Enter] key to continue..."
readEnterKey;;
      "3")echo "-------------------------------"        
          read -p "Enter Permissions  " perm 
          setfacl -m o::$perm $f_path
          read -p "Press [Enter] key to continue..."
readEnterKey;;
      "*")echo "********Invalid Choice**********"
          read -p "Press [Enter] key to continue..."
readEnterKey;;
      esac 
      else 
          echo "********Invalid Choice**********"     
          read -p "Press [Enter] key to continue..."
readEnterKey
      fi  
else 
     echo "***********Good Bye***********"
     exit 0   
fi
done
