# Day 10: Multiplication Table

## Theory
A multiplication table is a list of the results of multiplying a number by other numbers. It’s a good exercise for practicing loops and displaying formatted output.

### Key Concepts:
- Use a **nested loop** to generate the table.
- Display the results in a grid format.

### Example:
n = 3
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i} * {j} = {i * j}", end="\t")
    print()  # New line after each row
