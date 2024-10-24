# Day 5: Practice Exercise

## Exercise
# Write a program that receive 2 numbers, then prints their sum, difference, product, and quotient. Additionally, print a message if the second number is zero, indicating that division cannot be performed.

# Take two numbers as input
a = 10
b = 5

# Print results
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)

if b != 0:
    print("Quotient:", a / b)
else:
    print("Division by zero is not allowed.")
