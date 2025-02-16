
"""
Situation/Problem:
An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists). 
Given an array arr[] of size N, Return the index of any one of its peak elements.
Intuition/Solucion:
We can do the linear search and check the given condition (arr[i] > arr[i-1] and arr[i] > arr[i+1])  satisfies the element or not.
Implementation:
Iterate the whole array and check whether the following condition satisfies (arr[i] > arr[i-1] and arr[i] > arr[i+1]) .
for the boundary elements just check for the adjacent which exist and if the condition satisfies just return the index.
"""

def peakElement(arr, n):
    """Given an array arr[] of size N, Return the index of any one of its peak elements."""
    # this solution is slower than binary search with no enumerate
    if n == 1:
        return 0
    for i, a in enumerate(arr):                 # enumerate like index
        if i > 0 and i < n-1:
            if a > arr[i-1] and a > arr[i+1]:   # is in between the elements of arr
                return i 
        if i == 0 and a > arr[1]:               # is the first element
            return i
        if i == n-1 and a > arr[i-1]:           # is the last element
            return i
    return -1

peak = peakElement([2, 2], 2)

if peak >= 0 :
    print(f"One peak found in element: {peak}")
else:
    print(f"No peak found at all.")