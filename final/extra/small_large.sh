#!/bin/bash

read -p "Enter some numbers: " -r -a arr

largest=${arr[0]}

for i in "${arr[@]}"; do
    if ((i > largest)); then
        largest=$i
    fi
done

echo "Largest element is $largest"

smallest=${arr[0]}

for i in "${arr[@]}"; do
    if ((i < smallest)); then
        smallest=$i
    fi
done

echo "Largest element is $smallest"
