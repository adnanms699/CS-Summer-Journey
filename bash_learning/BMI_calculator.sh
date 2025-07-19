#!/bin/bash
while true; do

read -p "What is your Name?" name
read -p "What is your Age?" age

     if [[ "$name" =~ ^[a-zA-Z]+$ ]] && (( ${#name} >= 8 )) && [[ "$age" =~ ^[0-9]+$ ]]; then
       echo "Valid info to proceed"
       break
    else
      echo "Invalid info try again"
    fi
done

read -p "What is your original weight in KGs ?" Weight
read -p "What is your real height in CM ?" Height
Heightmeters=$(echo "scale=2; $Height / 100" | bc)

BMI=$(echo "scale=2; $Weight / ($Heightmeters * $Heightmeters)" | bc)

echo "Your BMI is: $BMI"

if (( $(echo "$BMI < 18.5" | bc -l) )); then
   ans="Underweight"
   echo "Underweight"
elif (( $(echo "$BMI < 25" | bc -l) )); then
   ans="Healthy"
   echo "Healthy"
elif (( $(echo "$BMI < 30" | bc -l) )); then
   ans="OVERWEIGHT"
   echo "Overweight"
else
   ans="Obeeeeeeeese"
   echo "Obeeese"
fi
case "$ans" in
     Underweight)
           echo "Your food suggestions are eat good food with high fat and carbs"
           ;;
     Healthy)
          echo "Your all set to achieve 100 years of life in this earth"
          ;;
     OVERWEIGHT)
          echo "Dude leave some food for us and your food suggestions are fast 3 days per week and reduce fat : carbs"
          ;;
     Obeeeeeeeese)
          echo "Wooow your soo rich that you eat the whole families food... you need to fast 30days per month"
          ;;
     *)
          echo "Stop eating"
          ;;
esac

echo "$name - $age - $Weight - $Height - $BMI - $ans" >> BMI_calculation.txt

