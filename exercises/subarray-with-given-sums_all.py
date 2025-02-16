"""
Given an unsorted array A of size N that contains only non negative integers, 
find a continuous sub-array that adds to a given number S 
and return the left and right index(1-based indexing) of that subarray.

In case of multiple subarrays, return the subarray indexes which come first on moving from left to right.
"""

# simple test samples
from functools import reduce

def findAllSum(numbers,s):
    n = len(numbers)
    i = 0
    j = 1
    sum = 0
    while i < n:
        while j <= n:
            sum = reduce(lambda x, y: x+y, list(numbers[i:j]))
            if sum == s:
                print(sum, i+1, j)
            elif sum > s:
                break
            j += 1
        sum = 0
        i += 1
        j = i+1
    print(f"fin con s = {s} y sum = {sum}.")

def findSum(numbers,n ,s):
    i = 0
    j = 1
    sum = 0
    while i < n:
        while j <= n:
            sum = reduce(lambda x, y: x+y, list(numbers[i:j]))
            if sum == s:
                print(sum, i+1, j)
            elif sum > s:
                break
            j += 1
        sum = 0
        i += 1
        j = i+1
    print(f"fin con s = {s} y sum = {sum}.")              

"""
Testing routine
First test with some simple and accurate samples
Next test with random samples
"""
# Here's a list of numbers for testing findAllSum
numbers = [0, 1, 0, 1]
n = len(numbers)
s = 1
findAllSum(numbers, s)


