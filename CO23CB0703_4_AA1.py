def recursive_function(n):
    """This function returns multiple values using recursion."""
    if n == 0:
        return 0, 1  # base case
    else:
        a, b = recursive_function(n-1)
        return b, a + b

# Call the recursive_function with an argument of 5
result1, result2 = recursive_function(5)

# Print the results
print("Result 1:", result1)
print("Result 2:", result2)
