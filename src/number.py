# Commonly used number-related functions

def sieve(n):
    """Sieve of Eratosthenes. Returns a list"""
    nums = [0] * n
    for i in range(2, int(n**0.5)+1):
        if nums[i] == 0:
            for j in range(i*i, n, i):
                nums[j] = 1

    return [i for i in range(2, n) if nums[i] == 0]


def sieve_set(n):
    return set(sieve(n))


def is_prime(n):
    """Returns whether a number is prime or not"""
    if n < 2: return False
    return all(n%i for i in range(2, int(n**0.5)+1))


def is_square(n):
    """Returns if a number is square without floating point math. Credit: Alex Martelli"""
    x = n // 2
    seen = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True


def prime_factors(n):
    factors = []
    m = n
    prime = False
    while not prime:
        prime = True
        for i in range(2, int(m**0.5)+1):
            if m%i == 0:
                m //= i
                factors.append(i)
                prime = False
                break

    return factors + [m]


if __name__ == "__main__":
    pass
