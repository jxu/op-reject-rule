# c+1 = (b+1)^2 / (a+1)
import number,time
def S(n):
    primes = number.sieve(n)
    sp = set(primes)

    #for ai in range(len(primes)):
    #    print(primes[ai])
    #    for bi in range(ai+1, len(primes)):
    #        a = primes[ai]
    #        b = primes[bi]



S(10**4)

start = time.clock()
for a in range(10**6):
    if a%1000 == 0: print(a)
    for b in range(a, 10**4 * int((a+1)**0.5)):
        pass

print(time.clock()-start)