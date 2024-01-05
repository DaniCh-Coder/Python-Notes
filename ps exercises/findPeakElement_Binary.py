"""
Situation/Problem:
An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists). 
Given an array arr[] of size N, Return the index of any one of its peak elements.
Intuition/Solucion:
We will use the concept of binary search to find any peak element index
if we are at any current index by comparing it with its neighbour, 
we can tell whether at least one peak element lies on its left or right 
and accordingly we can search on that half of the array i.e, we can do binary search.
"""

def findPeakUtil(arr, low, high, n):
    """Given an array arr[] of size N, Return the index of any one of its peak elements."""
    # using only array with binary search
    mid = (low+high) // 2 
    # mid=0 or arr[mid-1]<=arr[mid]
    # and
    # mid==n-1 or arr[mid+1]<=arr[mid]
    if (mid==0 or arr[mid-1]<=arr[mid]) and (mid==n-1 or arr[mid+1]<=arr[mid] ):
        # print(1)
        return mid
    elif (mid>0 and arr[mid-1]>arr[mid]):
        # print(2)
        return findPeakUtil(arr,low,mid-1,n)
        # else recurse for the upper half
    else :
        # print(3)
        return findPeakUtil(arr,mid+1,high,n)   

def peakElement(arr, n):
        return findPeakUtil(arr,0,n-1,n)

"""
Testing routine
First test with some simple and accurate samples
Next test with random samples
"""
# import random from python library for random samples generation
import random as rnd

# simple samples
# n = 3
# arr = [8,9,10]
# n = 0
# arr = []

# random samples
n = rnd.randrange(25)
arr = [ rnd.randrange(10) for i in range(n)]

if n and n == len(arr):
    peak = peakElement(arr, n)
else:
    peak = -1

print(f"Array size: {n}. Elements: {arr}.")
if peak >= 0:
    print(f"One peak found in element: {peak}")
else:
    print(f"No peak found at all.")