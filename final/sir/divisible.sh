#!/bin/bash

sum=0

for i in {50..100}; do
    if ((i % 3 == 0 && i % 5 != 0)); then
        echo "Processing number: $i"
        sum=$((sum + i))
    fi
done

echo "Sum of numbers divisible by 3 but not by 5: $sum"
