#!/bin/bash 
read -p "Give me the directory or file to see if it exists:" Name
read -p "Give me the file name to see its existance:" File
if [ ! -d "$HOME/$Name" ]; then
   echo "The directory does not exists"
else
   echo "IT DOES EXIST"
fi

if [ ! -f "$File" ]; then
   echo "The file does not exist"
else
   echo "It exists"
fi
