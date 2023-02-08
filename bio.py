name = input("What is your name? ")
color = input("What is your favorite color? ")
age = int(input("How old are you today? "))

# print(name, end=" ")
# print("is " + str(age) + " years old", end=" ")
# print("and loves the color " + color + ".", end=" ")

# Using a single line to print

print(name, 'is', age, 'years old and loves the color', color + '.')

# sep=" " which is single space is the default seperator option
# you can use other things to put inbetween to seperate such as: 
# sep=", "