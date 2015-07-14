# Alternatively, product of small primes (2*3*5*7*11*13*17)

from number import phi

max_d = 0
max_n = 0
for n in range(1, 1000001):
    d = n/phi(n)
    if d > max_d:
        max_d = d
        max_n = n
        print(n, d)
