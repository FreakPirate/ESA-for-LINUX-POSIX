#!/bin/bash

#$source_path= $1 ;  $destination_path=$2 

sudo getfacl $1| sudo setfacl --set-file=- $2 
