# Day 9: Nest Loops and Conditions

# Get user input
n = 10

# Nested loop to print pairs of numbers
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            print(f"Pair: ({i}, {j}) - i and j are equal")
        else:
            print(f"Pair: ({i}, {j})")