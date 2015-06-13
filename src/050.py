import number
primes = number.sieve(10**6)

max_l = best_p = 0
for i in range(len(primes)-1, 0, -1): # Larger numbers have longer sequences
    if primes[i] < 9*10**5: break

    for j in range(10): # Starting prime
        s = l = 0
        for k in range(j, len(primes)):
            s += primes[k]
            l += 1
            if s >= primes[i]: break

        if s == primes[i]:
            print(s, primes[j], l)
            if l > max_l:
                max_l = l
                best_p = s

            break

print(best_p)
