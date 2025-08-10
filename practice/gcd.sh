#!/bin/bash

read -p "Enter 1st number: " -r a
read -p "Enter 2nd number: " -r b

if ((a > b)); then
    num1=$a
    num2=$b
else
    num1=$b
    num2=$a
fi

until ((num2 == 0)); do
    q=$((num1 / num2))
    r=$((num1 % num2))
    num1=$num2
    num2=$r
done

echo "GCD of $a and $b is $num1"

lcm=$(((a * b) / num1))

echo "LCM of $a and $b is $lcm"
