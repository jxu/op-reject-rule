from number import sieve

primes = sieve(10**6)

n = 10**18
def f(c, i):
    s = n // c

    for j in range(i, len(primes)):
        if c * primes[j]**3 > n: break
        
        for k in range(3, 100):
            y = c * primes[j]**k
            if y > n: break
            
            s += f(y, j+1)
    return s

print(f(1, 0))
