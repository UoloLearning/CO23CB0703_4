def count_down_recursive(n):
    """This function counts down from n to 0 using recursion."""
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        count_down_recursive(n-1)

# Call the count_down_recursive function with an argument of 5
count_down_recursive(5)
