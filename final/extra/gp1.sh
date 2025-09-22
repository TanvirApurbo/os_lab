#!/bin/bash

read -p "Enter the value of n: " n

sum=0
for ((i = 1; i <= n; i++)); do
    sum=$((sum + i * i))
done

echo "Sum of squares from 1 to $n is $sum"

# For odd numbers
read -p "Enter the number of odd terms (n): " n

sum=0
for ((i = 0; i < n; i++)); do
    odd=$((2 * i + 1))
    sum=$((sum + odd * odd * odd))
done

echo "Sum of cubes of first $n odd numbers is $sum"

# For even numbers
read -p "Enter the number of even terms (n): " n

sum=0
for ((i = 1; i <= n; i++)); do
    even=$((2 * i))
    sum=$((sum + even * even * even))
done

echo "Sum of cubes of first $n even numbers is $sum"
