#!/bin/bash

read -p "Enter a number: " -r num

temp=$num
sum=0
while ((temp > 0)); do
    r=$((temp % 10))
    sum=$(((sum * 10) + r))
    temp=$((temp / 10))
done

echo "Reverse of $num is $sum"
