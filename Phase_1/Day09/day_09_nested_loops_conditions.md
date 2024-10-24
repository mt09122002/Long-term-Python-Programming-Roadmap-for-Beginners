# Day 9: Nest Loops and Conditions

## Theory

Nesting loops means placing one loop inside another. Similarly, you can nest conditions within other conditions. Nested loops and conditions are useful when you need to handle more complex logic, like iterating over multiple dimensions or applying multiple rules in a sequence.

### Key Concepts:

- **Nested loops:** One loop inside another.
- **Nested conditions:** An `if` statement inside another `if` statement.

### Example:

```python
for i in range(1, 4):
    for j in range(1, 4):
        if i == j:
            print(f"i and j are equal: {i}")
```
