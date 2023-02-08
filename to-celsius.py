#!/usr/bin/env python3.7

# Python implementation goes here

fahrenheit = float(input("What temperature (in Fahrenheit) would you like converted to Celsius? "))
celsius = (fahrenheit - 32) * 5 / 9

print(fahrenheit, "F is", round(celsius, 2), "C")

# Success!
# Created a script that prompts the user for some information 
# Converts it into a usable type
# Runs some calculations 
# Then prints those back out 