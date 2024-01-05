"""
Given an unsorted array A of size N that contains only non negative integers, 
find a continuous sub-array that adds to a given number S 
and return the left and right index(1-based indexing) of that subarray.

In case of multiple subarrays, return the subarray indexes which come first on moving from left to right.
"""

import random as rnd
from functools import reduce

def findSum(numbers,n ,s):
    i = 0
    j = 1
    sum = 0
    while i < n:
        while j <= n:
            sum = reduce(lambda x, y: x+y, list(numbers[i:j]))
            if sum == s:
                return [i+1, j]
            elif sum > s:
                break
            j += 1
        sum = 0
        i += 1
        j = i+1
    return [-1]    

"""
Testing routine
First test with some simple and accurate samples
Next test with random samples
"""
# Here's a list of numbers for testing findAllSum
# numbers = [0]
# n = len(numbers)
# s = 0

# numbers = [1,2,3,4,5,6,7,8,9,10]
# n = len(numbers)
# s = 15

# numbers = [1, 2, 3, 7, 5]
# n = len(numbers)
# s = 12 # res 2 4



# random samples
n = rnd.randrange(50)
numbers = [ rnd.randrange(9) for i in range(n)]
s = rnd.randrange(15)
print(s, " -- ", numbers)

ans = findSum(numbers, n, s)
print(ans, end=' ')

