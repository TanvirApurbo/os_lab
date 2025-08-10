#!/bin/bash

# Check if exactly 3 arguments are given
if [ $# -ne 3 ]; then
    echo "Usage: $0 num1 num2 num3"
    exit 1
fi

a=$1
b=$2
c=$3

arr=($a $b $c)

sorted=$(printf "%s\n" "${arr[@]}" | sort -n)

echo "Numbers in ascending order:"
echo "$sorted"
