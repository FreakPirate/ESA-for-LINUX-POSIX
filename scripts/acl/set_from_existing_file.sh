#!/bin/bash

#$source_path= $1 ;  $destination_path=$2 

getfacl $1| setfacl --set-file=- $2 
