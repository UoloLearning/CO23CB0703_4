def fibonacci_recursive(n):
    """This function generates the Fibonacci sequence using recursion."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Generate the first 10 terms of the Fibonacci sequence
for i in range(10):
    print(fibonacci_recursive(i))
