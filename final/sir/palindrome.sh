#!/bin/bash

read -p "Enter a string: " -r str

rev=""

for ((i = ${#str} - 1; i >= 0; i--)); do
    rev="$rev${str:i:1}"
done

if [[ "$rev" == "$str" ]]; then
    echo "$str is a palindrome!"
else
    echo "$str is not a palindrome."
fi
