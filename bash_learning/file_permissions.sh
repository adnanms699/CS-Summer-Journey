#!/bin/bash
read -t 15 -p "Enter the user name of the owner to access file permissions and change it: " User_name

if [[ "$(whoami)" != "$User_name" ]]; then 
  echo "Scammer spotted, womp womp cry more"
  exit 1
else
  echo "Welcome owner!!!, have a good day ahead"
fi

read -p "Enter the file you want to change/view permissions for :" filename

if [ ! -e "$filename" ]; then
  echo "File does not exist"
  exit 1
fi

echo "Current permissions"
ls -l "$filename"

read -p "Write the type/kind of permission you want to change:" PermissionType

chmod "$PermissionType" "$filename"

echo "Permission Updated"
ls -l "$filename"
