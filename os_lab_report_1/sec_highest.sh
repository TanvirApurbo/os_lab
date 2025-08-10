#!/bin/bash

read -p "Enter numbers separated by space: " -a numbers

sorted_numbers=($(for num in "${numbers[@]}"; do echo $num; done | sort -n))
echo "Sorted numbers: ${sorted_numbers[*]}"

if ((${#numbers[@]} < 2)); then
    echo "Please enter at least 2 numbers"
    exit 1
fi

if ((numbers[0] > numbers[1])); then
    max1=${numbers[0]}
    max2=${numbers[1]}
else
    max2=${numbers[0]}
    max1=${numbers[1]}
fi

for ((i = 2; i < ${#numbers[@]}; i++)); do
    if ((numbers[i] > max1)); then
        max2=$max1
        max1=${numbers[i]}
    elif ((numbers[i] > max2)); then
        max2=${numbers[i]}
    fi
done

echo "Second highest number is: $max2"
