# This sript take a number from the user and calculates its factorial.
# This implementation uses an iterative approach.
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Alternatively, you can use a recursive approach:
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    

def main():
    try:
        number = int(input("Enter a non-negative integer: "))
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = factorial(number)
            print(f"The factorial of {number} is {result}.")
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")
        
if __name__ == "__main__":
    main()

