"""
Given an unsorted array A of size N that contains only non negative integers, 
find a continuous sub-array that adds to a given number S 
and return the left and right index(1-based indexing) of that subarray.

In case of multiple subarrays, return the subarray indexes which come first on moving from left to right.
"""

import random as rnd
#Function to find a continuous sub-array which adds up to a given number.

def subArraySum(arr, n, sum_): 
    # Initialize curr_sum as value of first element and starting point as 0 
    A = []
    curr_sum = arr[0]
    start = 0

    # Add elements one by one to curr_sum and if the curr_sum exceeds the sum, then remove starting element 
    i = 1
    while i <= n:
    
        # If curr_sum exceeds the sum, then remove the starting elements
        while curr_sum > sum_ and start < i-1:
            curr_sum = curr_sum - arr[start]
            start += 1
            
        # If curr_sum becomes equal to sum, then return true
        if curr_sum == sum_:
            A.append(start+1)
            A.append(i)
            return A

        # Add this element to curr_sum
        if i < n:
            curr_sum = curr_sum + arr[i]
            i += 1

        # If we reach here, then no subarray
    A.append(-1)
    return A

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

ans = subArraySum(numbers, n, s)
print(ans, end=' ')

