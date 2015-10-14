from number import sieve
primes = sieve(10**8 // 2)
count = 0
for i in range(len(primes)):
    for j in range(i+1):
        if primes[i] * primes[j] >= 10**8: break
        count += 1
print(count)