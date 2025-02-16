# Python program to find sum of array 
# elements using recursion. 

# Return sum of elements in A[0..N-1] 
# using recursion. 
def _findSum(arr, N): 
	if N <= 0: 
		return 0
	else: 
		return _findSum(arr, N - 1) + arr[N - 1] 

# driver code 
arr =[] 
# input values to list 
arr = [1, 2, 3, 4, 5] 

# calculating length of array 
N = len(arr) 

ans =_findSum(arr,N) 
print (ans) 

# This code is contributed by Khare Ishita 
