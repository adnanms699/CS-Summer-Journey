#!/bin/bash

read -t 10 -p "what is your name:" user_input
echo "$user_input $1 $2"

if [[ "$user_input" =~ ^[a-zA-Z]+$ && ${#user_input} -ge 5 ]]; then
    echo "Valid user_name"
else
    echo "InValid user_name - only letters are allowed, time limit is 10sec and the input should have a min of 5 characters"
fi
