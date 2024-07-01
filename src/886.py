from functools import cache
from number import sieve

def in_bit(b, i):
    return bool(b & (1 << i))

def set_bit(b, i):
    return b | (1 << i)

def clear_bit(b, i):
    return b & ~(1 << i)

primes = sieve(34)

# TODO: replace with better function
def coprime(a, b):
    return not any(a%p == 0 and b%p == 0 for p in primes)

#print(coprime(6,9))
#print(coprime(2,3))

def even_bit_count(n):  # bits 0, 2, 4, 6, ...
    return (n & 0x55555555).bit_count()

def odd_bit_count(n):
    return (n & 0xaaaaaaaa).bit_count()

n = 20

@cache
def f(seen, k):
    #print(bin(seen), k)
    if seen.bit_count() == 1: return 1

    # optimization
    # n=20.
    # without even-odd: hits=12271501 size=2831840
    # with even-odd:    hits= 3483249 size=1214491
    d = even_bit_count(seen) - odd_bit_count(seen)
    z = seen.bit_count()
    #if abs(even_bit_count(seen) - odd_bit_count(seen)) > 1: return 0

    if k%2 == 0:
        if z%2 == 0 and d != 0: return 0
        if (z%2) != 0 and d != 1: return 0

    if k%2 == 1:
        if z%2 == 0 and d != 0: return 0
        if z%2 != 0 and d != -1: return 0


    r = 0
    for newk in range(2, n+1):
        if in_bit(seen, newk) and coprime(k, newk):
            r += f(clear_bit(seen, k), newk)

    return r

r = 0
for k in range(2, n+1):
    x = ((1 << (n-1)) - 1 ) << 2
    #print(bin(x))
    z = f(x, k)
    #print(k, z)
    r += z

print(f.cache_info())
print(r)
