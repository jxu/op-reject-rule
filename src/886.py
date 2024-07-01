from functools import cache

def in_bit(b, i):
    return bool(b & (1 << i))

def set_bit(b, i):
    return b | (1 << i)

def clear_bit(b, i):
    return b & ~(1 << i)

primes = (2, 3, 5, 7, 11, 13, 17)

# TODO: replace with better function
def coprime(a, b):
    return not any(a%p == 0 and b%p == 0 for p in primes)

#print(coprime(6,9))
#print(coprime(2,3))

def odd_bit_count(n):
    return (n & 0x55555555).bit_count()

def even_bit_count(n):
    return (n & 0xaaaaaaaa).bit_count()

n = 10

@cache
def f(seen, k):
    #print(bin(seen), k)
    if seen.bit_count() == 1: return 1

    # optimization
    # n=20. without even-odd: size=2978690
    # with even-odd: size=1972297
    d = even_bit_count(seen) - odd_bit_count(seen)
    z = seen.bit_count()
    if abs(even_bit_count(seen) - odd_bit_count(seen)) > 1: return 0
    if k%2 == 0:
        if z%2 == 0 and d != 0: return 0
        if (z%2) != 0 and d != 1: return 0

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
