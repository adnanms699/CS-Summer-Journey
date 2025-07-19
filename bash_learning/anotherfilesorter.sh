#!/bin/bash

read -p "Give a directory name from your system to scan for the type of extensions:" Directory

if [ -d ~/"$Directory" ]; then
  echo "Directory exists"
else
  echo "Directory does not exist"
  exit 1
fi

echo -e "There are $(find ~/"$Directory" -type f -name "*.sh" | wc -l) .sh files\nThere are $(find ~/"$Directory" -type f -name "*.txt" | wc -l) .txt files in the chosen directory"


