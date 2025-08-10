#!/bin/bash

read -p "Enter length of a rectangle: " l
read -p "Enter width of a rectangle: " w

area=$(echo "scale=2; $l*$w" | bc)

perimeter=$(echo "scale=2; 2*($l+$w)" | bc)

echo "Area of your rectangle is $area"
echo "Perimeter of your rectangle is $perimeter"
