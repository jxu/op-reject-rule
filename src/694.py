from number import sieve

primes = sieve(10**6)

n = 10**18
def f(c, i):
    s = n // c

    for j in range(i, len(primes)):
        y = c * primes[j]**3  # minimum y
        if y > n: break  # important: exit j loop early
       
        while y <= n: 
            s += f(y, j+1)
            y *= primes[j]
    
    return s

print(f(1, 0))

