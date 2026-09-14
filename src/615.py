# Dijkstra-like search idea:
# Start with base 2^N, then multiply by 2 or p/2 for odd p
# Priority queue keeps searching smallest new nodes
# Got away with using floating point because div by 2 is exact!
# Can't believe it was this easy given the fastest solvers list...

from number import sieve
from heapq import heappush, heappop

bound = 10**5  # upper bound to tune
N = 10**6
primes = sieve(2 * bound)

# scaling factors in order are 3/2, 2, 5/2, 7/2, ...
scaling = [3/2, 2] + [p/2 for p in primes[2:]]
visited = []

# store s, min_i
h = [(1,0)]

for t in range(N):
    s, min_i = heappop(h)
    visited.append(s)
    #print(s)

    # add new frontier nodes
    for i in range(min_i, len(primes)):
        x = s * scaling[i]
        if x > bound: break

        heappush(h, (x, i))

# recover number
x = visited[-1]
pow2 = 0
while int(x) != x:
    x *= 2
    pow2 += 1

print(x, pow2)
print(int(x) * pow(2, N - pow2, 123454321) % 123454321)