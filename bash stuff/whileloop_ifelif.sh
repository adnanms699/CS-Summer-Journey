#!/bin/bash
read -t 15 -p "Enter your good name:" Name

while true; do
    read -p "Enter your current Age:" Age

    if [[ "$Age" =~  ^[0-9]+$ ]]; then
      if (( Age > 80 )); then
        echo "Yoo your lil too old grandpa"

      elif (( Age > 17  )); then
        echo "Age criteria met!!"
        break
      else
        echo "Grow up you lil kiddo!"
      fi
    else
        echo "Enter digits only"
    fi
done

if [[ "$Name" =~ ^[a-zA-Z]+$ && ${#Name} -ge 10 ]]; then
    echo "Valid user name"
else
    echo "Invalid user name"
fi

