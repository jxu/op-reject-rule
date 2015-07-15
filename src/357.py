# Numbers must be square-free (otherwise div by p), and must be p-1
from number import sieve
import time

start = time.process_time()

def f(N_MAX):
    primes = sieve(N_MAX)
    div_squares = [x**2 for x in sieve(int(N_MAX**0.5))]


    s = 0
    for p in primes:
        #squarefree = all((p-1)%s != 0 for s in div_squares)
        #if squarefree:
        s += 1

    return s




print(f(10**8))
print(time.process_time() - start)
