# Commonly used prime number functions
def sieve(n):
    """Sieve of Eratosthenes. Returns a set"""
    nums = [0] * n
    for i in range(2, int(n**0.5)+1):
        if nums[i] == 0:
            for j in range(i*i, n, i):
                nums[j] = 1
        
    return set(i for i in range(2, n) if nums[i] == 0)


def is_prime(n):
    """Returns whether a number is prime or not"""
    if n < 2: return False
    return all(n%i for i in range(2, int(n**0.5)+1))


if __name__ == "__main__":
    pass
