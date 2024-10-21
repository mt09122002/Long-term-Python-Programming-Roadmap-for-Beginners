# Take two numbers as input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Print results
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b if b != 0 else "Division by zero is not allowed.")