#!/bin/bash

num=-1
until ((num > 1)); do
    read -p "Enter a number: " -r num
done

if ((num == 2)); then
    echo "2 is a prime number"
    exit
fi

for ((i = 2; i < num; i++)); do
    if ((num % i == 0)); then
        echo "$num is not a prime number"
        echo "$i is the factor of $num"
        exit
    fi
done

echo "$num is a prime number"

is_prime() {
    local num=$1

    if ((num <= 1)); then
        return 1 # false
    fi

    if ((num == 2)); then
        return 0 # true
    fi

    for ((i = 2; i < num; i++)); do
        if ((num % i == 0)); then
            return 1 # false
        fi
    done

    return 0 # true
}

# read -p "Enter a number: " -r num

for i in {1..100}; do
    if is_prime "$i"; then
        echo "$i is a prime number"
    # else
    #     echo "$num is not a prime number"
    fi
done
