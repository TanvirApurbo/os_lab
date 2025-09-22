#!/bin/bash

read -p "Enter radius of a circle: " r

circumference=$(echo "scale=2; 2*3.14*$r" | bc)
echo "Circumference of your circle is $circumference"

read -p "Enter length of a rectangle: " l
read -p "Enter width of a rectangle: " w

perimeter=$(echo "scale=2; 2*($l+$w)" | bc)
echo "Perimeter of your rectangle is $perimeter"

read -p "Enter side a of triangle: " a
read -p "Enter side b of triangle: " b
read -p "Enter side c of triangle: " c

perimeter_triangle=$(echo "scale=2; $a+$b+$c" | bc)
echo "Perimeter of your triangle is $perimeter_triangle"
