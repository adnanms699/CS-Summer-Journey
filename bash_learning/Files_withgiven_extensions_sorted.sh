#!/bin/bash
read -p "Give me your extension to search for:" File_Extenstion
lower="${File_Extenstion,,}"

if [ "$lower" = ".sh" ]; then
  find ~/Adnan_learnings -type f -iname "*$File_Extenstion" -exec stat -c"%s %n" {} \; | sort -nr
elif [ "$lower" = ".txt" ]; then
  find ~/Adnan_learnings -type f -iname "*$File_Extenstion" -exec stat -c"%s %n" {} \; | sort -nr
else
   echo "NO SUCH FILE EXISTS"
fi
