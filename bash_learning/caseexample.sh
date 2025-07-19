#!/bin/bash
read -p "What is your Name:" name

if [[ "$name" =~ ^[a-zA-Z]+$ && ${#name} -ge 8 ]]; then
  echo "Valid Username"
else
  echo "Invalid Username"
fi

read -p "What is your current age:" age

if [[ "$age" =~ ^[0-9]+$ ]]; then
   if (( age > 17 )); then
     echo "Age criteria met for therapy"
  else
     echo "Dont watch traumatic movies kiddo"
     exit 1
  fi
else
   echo "Enter a valid number"
fi

if [[ "$name" =~ ^[a-zA-Z]+$ ]] && (( ${#name} >= 8 )) && [[ "$age" =~ ^[0-9]+$ ]]; then
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] - "$name" - "$age" - Therapy" >> Therapylist.txt
else
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] - "$name" - "$age" - No need Therapy" >> Therapylist.txt
fi

read -p "What is your current mood now?" Mood

Happy_quotes=("YAAAY YOU CAN DO IT" "LESSGOOO YOU DID IT" "LIU LIU LIU")
Sad_quotes=("SO SAD" "GET UP GO HUNT" "BRUH DONT BE SAD")
Broken_quotes=("DAAAAMN" "DANG" "Its alr")

random_index=$((RANDOM % ${#Happy_quotes[@]}))
Random_Index=$((RANDOM % ${#Sad_quotes[@]}))
RANDOM_INDEX=$((RANDOM % ${#Broken_quotes[@]}))

mood="${Mood,,}"

case "$mood" in
     happy)
         echo "The motivational qoutes for your current mood is: ${Happy_quotes[$random_index]}"
         ;;

     sad)
         echo "The motivational quotes for your current mood is: ${Sad_quotes[$Random_Index]}"
         ;;

     broken)
         echo "The motivational quotes for your current mood is: ${Broken_quotes[$RANDOM_INDEX]}"
         ;;

     *)
         echo "GO TO A THERAPIST!!"
         ;;
esac
