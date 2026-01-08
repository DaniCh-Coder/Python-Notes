def sum_numbers(n):
    """Sum all numbers from 1 to n (inclusive)."""
    return sum(range(1, n + 1))

# Example usage
number = int(input("Enter a number: "))
result = sum_numbers(number)
print(f"The sum of numbers from 1 to {number} is: {result}")