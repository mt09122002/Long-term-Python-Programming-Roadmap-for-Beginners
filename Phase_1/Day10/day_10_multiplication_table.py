# Day 10: Multiplication Table

# Get user input
n = int(input("Enter a number: "))

# Generate multiplication table
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i} * {j} = {i * j}", end="\t")
    print()  # New line after each row