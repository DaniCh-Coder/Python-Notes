# serch find elements in arrays 
arr = [1, 2, 3, 4, 3] # list to be searched in
x = 3               # element to be searched
n = len(arr)

# find x using list comprehension
verdad = [ x in arr ]
print(verdad)

# find x using count method
cuenta = arr.count(x)
print(cuenta)

alguno = any(x for x in arr)
print(alguno)

# index = arr.index(x)
# print(index)
try:
    # check if string is present in list
    index = arr.index(x)
    print(f'{x} is present in the list at index {index}')
except ValueError:
    print(f'{x} is not present in the list')

# Check if string is present in each string in the list using enumerate
valpos_x = [(arr[i], i) for i in range(len(arr)) if arr[i] == x]
print(valpos_x)

# Checking the position through a list comprehension
pos_x = [i for i in range(len(arr)) if arr[i] == x]
print(pos_x)
print(pos_x[0])