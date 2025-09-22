#!/bin/bash

read -p "Enter a number: " -r num

temp=$num
digits=()

while ((temp != 0)); do
    digits+=($((temp % 10)))
    temp=$((temp / 10))
done

n=${#digits[@]}
sum=0

for d in "${digits[@]}"; do
    power=$(echo "$d^$n" | bc)
    sum=$((sum + power))
done

if ((sum == num)); then
    echo "$num is an Armstrong number."
else
    echo "$num is NOT an Armstrong number."
fi
