# Swap the values of two variables

print("Before swapping:")
v1 = int(input('Enter first number: '))
v2 = int(input('Enter second number: '))

v1, v2 = v2, v1

print("After swapping:")
print(f"First number: {v1}")
print(f"Second number: {v2}")