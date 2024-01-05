# max and min in an array
a = [ 5, 2, 3, 4, 1]
n = len(a)
r = a[0], a[n-1]
print(f"(ini, fin): {r}")

# find min max with functions
minmax = min(a), max(a)
print(f"(min, max): {minmax}")

# better choise couse sort only one time
# sort to allocate min at the beggining and max at the end
a.sort()                # carefull sort() sort but return none
minmax = a[0], a[n-1]   # tuple with begin and end (min and max)
print(f"sorted (min, max): {minmax}")




