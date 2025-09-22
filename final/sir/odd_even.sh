#!/bin/bash

sum_even=0
sum_odd=0

read -p "Enter numbers separated by space: " -a numbers

for num in "${numbers[@]}"; do
	if ((num % 2 == 0)); then
		sum_even=$((sum_even + num))
	else
		sum_odd=$((sum_odd + num))
	fi
done

echo "Sum of even numbers: $sum_even"
echo "Sum of odd numbers: $sum_odd"
