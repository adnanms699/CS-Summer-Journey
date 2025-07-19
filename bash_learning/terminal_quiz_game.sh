#!/bin/bash

read -t 20 -p "When did World War 1 happen?" Ans
read -t 20 -p "Who is the 1st Prime Minister of India?" Answer
read -t 20 -p "Which is the most populated country in 2025?" Answers

score=0

if [ "$Ans" -eq 1914 ]; then
  ((score++))
else
  ((score--))
  echo "Quiz over, try again when your smart enough"
  break
fi

if [ "${Answer,,}" == "nehru" ]; then
  ((score++))
else
  ((score--))
fi

if [ "${Answers,,}" == "india" ]; then
  ((score++))
else
  ((score--))
fi

printf "%s\n" "$score"

if [ "$score" -gt 2 ]; then
  echo "Your better than 90% of Indians"
else
  echo "You don't deserve to be an Indian"
fi
