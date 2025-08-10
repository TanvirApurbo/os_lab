#!/bin/bash

for i in {1..500}; do
    if ((i % 5 == 0 && i % 7 == 0)); then
        echo "$i"
    fi
done
