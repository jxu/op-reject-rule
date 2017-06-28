# Ref: A037992. For n = p1^a1...p1^ak, d(n) = (1 + a1)...(1 + ak)
# Write 1 + ai = 2^mi, m1 + m2 + ... + mk = 500500
# Significantly better algorithm running in one pass
# (credit: tinnderbox https://projecteuler.net/thread=500#195005)
# Call P(n) the smallest number with 2^n divisors. To get sum of mi from n-1 to
# n+1, one mi must be increased. Since ai = 2^mi - 1, ai are for ex. 3, 27, 729.
# These can be seen as 3, 3*9, 3*9*81. So to increase mi, multiply by last
# factor squared. Keep potential factors in a min queue.

from number import sieve
from heapq import heappush, heappop, heapify

LIMIT = 500500
min_queue = sieve(10**7)[:LIMIT]
max_prime = min_queue[-1]
heapify(min_queue)

ans = 1
for i in range(LIMIT):
    factor = heappop(min_queue)
    ans = (ans * factor) % 500500507
    if factor**2 < max_prime:
        heappush(min_queue, factor**2)

print(ans)
