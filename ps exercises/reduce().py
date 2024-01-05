"""
Given an unsorted array A of size N that contains only non negative integers, 
find a continuous sub-array that adds to a given number S 
and return the left and right index(1-based indexing) of that subarray.

In case of multiple subarrays, return the subarray indexes which come first on moving from left to right.
"""

# simple test samples
from functools import reduce


# A custom function that performs a complex operation
def complex_operation(x, y):
    # (This is a placeholder for your complex operation)
    return x * y

# Here's a list of numbers
numbers = [1, 2, 3, 4, 5]

# We'll use reduce to apply our custom function to these numbers
result = reduce(complex_operation, numbers)

print(result)

# Output:
# 120

result2 = reduce(lambda x, y: x+y, numbers)
print(result2)

print(list(numbers[1:]))

