#!/bin/bash

read -p "Enter a number: " num

fact=1
for ((i = 1; i <= num; i++)); do
    fact=$((fact * i))
done
echo "Factorial of $num is $fact"


# i=1
# while (( i <= num )); do
#     fact=$((fact * i))
#     ((i++))
# done
