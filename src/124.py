from number import sieve
primes = sieve(100000)

def rad(n):
    product = 1
    for p in primes:
        if n == 1: break
        if n % p == 0:
            product *= p
            while n % p == 0:
                n //= p

    return product

s = [(n, rad(n)) for n in range(1, 100001)]
s = sorted(s, key = lambda x: (x[1], x[0]))  # Sorting tricks from SO
print(s[9999])