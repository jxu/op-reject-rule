# Divisor sum function = sigma(n) = ((p_1^(a_1+1) - 1) / (p_1 - 1))*((p_2^(a_2+1) - 1) / (p_2 - 1))*...
# Current method: at least one of these factors must be a multiple of 2017
# Implement sigma efficiently later in number.py?
from number import sieve, is_prime

def S(n, d):
    s = 0
    # Test first factor (p^2-1)/(p-1) = p+1, so d|p+1, p < 10^11
    for f in range(d, n, d):
        if is_prime(f-1):
            print(f-1, 1)
            # Multiples of f-1
            ...

    # Test rest of factors
    primes = sieve(int(n**0.5)+1)
    for a_1 in range(2, 40):
        for p in primes:
            if p < n**(1/a_1):
                if (p**(a_1+1)-1)//(p-1) % d == 0:
                    print(p, a_1)



print(S(20, 7))