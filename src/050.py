# Bounded sum generation
# Solutions for 10^n starting with n=2: 41, 953, 9521, 92951, 997651, 9951191, 99819619
import number
primes = number.sieve(10**6)
sp = set(primes)

max_l = best_p = 0
for start in range(10): # Long sequences will start with low primes (test first 10)
    s = l = 0
    for i in range(start, len(primes)):
        l += 1
        s += primes[i]
        if s >= 10**6: break

        if s in sp and l > max_l:
            best_p = max(best_p, s)
            q = primes[start]
            max_l = l

print(best_p)
