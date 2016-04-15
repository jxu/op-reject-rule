# Numbers must be square-free (otherwise div by d), n = p-1
from number import sieve, prime_factors

primes = sieve(10**4)

def f(N_MAX):
    p_minus1 = [p-1 for p in primes]
    print(len(p_minus1))
        
    
    
    #squarefree = [1]*(N_MAX+1)
    
    #n_div2 = [0]*(N_MAX+1)
    #SQRT_N_MAX = int(N_MAX**0.5) + 1
    #for p in primes:
    #    if p > SQRT_N_MAX: break
    #    for i in range(p**2, N_MAX+1, p**2):
    #        squarefree[i] = 0



print(prime_factors(20))
print(prime_factors(100))


print(f(10**4))

