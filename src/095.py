# Sum of factors is product of prime powers that divide n
# ex. sum of factors of 120 = (1+2+2^2+2^3)(1+3)(1+5)
from number import sieve

primes = sieve(10**6)
sp = set(primes)

def proper_divisor_sum(n):  # credit: grimbal
    product = 1
    m = n
    for p in primes:
        if p*p > m: break

        s = 1
        pp = p
        while m % p == 0:
            s += pp
            pp *= p
            m //= p

        product *= s

    if m > 1: product *= m+1  # prime factor was > sqrt(n)
    return product - n


sums = [0] * 10**6
for i in range(10**6):
    sums[i] = proper_divisor_sum(i)

visited = [False]*10**6
max_chain = None
max_chain_len = 0

for i in range(10**6):
    if visited[i]: continue

    visited[i] = True
    seq = [i]
    valid_chain = True
    # Follow chain, marking as visited
    while sums[i] not in seq:
        i = sums[i]
        if i > 10**6:
            valid_chain = False
            break
        visited[i] = True
        seq.append(i)

    if valid_chain:
        chain = seq[seq.index(sums[i]):]  # Get cycle
        if len(chain) > max_chain_len:
            max_chain_len = len(chain)
            max_chain = chain

print(len(max_chain), max_chain)
print(min(max_chain))