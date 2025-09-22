#!/bin/bash

read -p "Enter radius of a circle: " r

area=$(echo "scale=2; 3.14*($r^2)" | bc)
echo "Area of your circle is $area"

circumference=$(echo "scale=2; 2*3.14*$r" | bc)
echo "Circumference of your circle is $circumference"
