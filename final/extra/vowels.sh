#!/bin/bash

read -p "Enter a string: " -r str

# Convert to lowercase so comparison is easier
str=$(echo "$str" | tr 'A-Z' 'a-z')

vowels=0
consonants=0

for ((i = 0; i < ${#str}; i++)); do
    ch=${str:i:1}
    if [[ $ch =~ [aeiou] ]]; then
        ((vowels++))
    elif [[ $ch =~ [a-z] ]]; then
        ((consonants++))
    fi
done

echo "Vowels: $vowels"
echo "Consonants: $consonants"
