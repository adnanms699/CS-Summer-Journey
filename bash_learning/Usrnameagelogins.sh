#!/bin/bash
read -t 15 -p "Enter your good name:" Name
read -p "Enter your current Age:" Age

    if [[ "$Age" =~  ^[0-9]+$ ]]; then
      if (( Age > 80 )); then
        echo "Yoo your lil too old grandpa"

      elif (( Age > 17  )); then
        echo "Age criteria met!!"
      else
        echo "Grow up you lil kiddo!"
      fi
    else
        echo "Enter digits only"
    fi


if [[ "$Name" =~ ^[a-zA-Z]+$ && ${#Name} -ge 10 ]]; then
    echo "Valid user name"
else
    echo "Invalid user name"
fi

Access=AccessGranted
Noaccess=NoAccess

if [[ "$Name" =~ ^[a-zA-z]+$ && "$Age" =~ ^[0-9]+$ ]]; then
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $Name - $Age - $Access" >> AccessGranted.txt
else
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $Name - $Age - $NoAccess" >> AccessGranted.txt
fi
