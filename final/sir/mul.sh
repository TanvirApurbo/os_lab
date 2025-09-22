#!/bin/bash

read -p "Enter a number: " -r n

for ((i = 1; i <= 10; i++)); do
    m=$((n * i))
    echo "$n x $i = $m"
done
