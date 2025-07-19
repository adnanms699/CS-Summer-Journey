#!/bin/bash

read -p "Give me your wanted file extension to see how many are there:" File_extension

echo "There are $(find ~/Adnan_learnings -type f -name "*$File_extension" | wc -l) '$File_extension' files in this folder."


