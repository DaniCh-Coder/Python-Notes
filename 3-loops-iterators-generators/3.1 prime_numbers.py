# Next code will check if one number is a prime number.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(11))  # Example usage

# Next code will detect the prime numbers in a given range.
def primes_in_range(start, end) -> list:
    """Returns a list of prime numbers in the given range [start, end].
       arguments:
         start -- the starting integer of the range
         end -- the ending integer of the range
    """
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

print(primes_in_range(10.5, 50))  # Example usage