"""A Change of Base

n  = d_0 a^0 + d_1 a^1 + ... + d_k a^k
2n = d_0 b^0 + d_1 b^1 + ... + d_k b^k

My initial implementation used a digit search from most significant down,
tracking valid ranges for n based on digits considered. 
Since 0 <= d_i < a, we can get any value for n, but the base b restricts what
ranges are possible. For example, for a = 3, b = 4, suppose k = 3 and d_3 = 1. 
Then n = 1xxx_3 and 2n = 1xxx_4.
This gives ranges 27 <= n < 54 and 64 <= 2n < 128. Searching through digits
further restricts possible ranges. Originally I tracked the max among all sols,
but since we want the max number, we can greedily search the digits in 
rev lex order.

The solution thread gave a much simpler formulation. Observe combining both
digit equations:
0 = d_0 (2 a^0 - b^0) + ... + d_k (2 a^k - b^k)
This gets rid of considering n. Use recursive search and pruning. 
In particular, I arrived at the same pruning strategy as eggben. 
Given d_k, d_{k-1}, ..., d_{j+1}, accept d_j if 
sum_{i=0..j-1} (a-1) |2 a^i - b^i| >= |sum_{i=j..k} d_i (2 a^i - b^i)|
otherwise the LHS, which represents the maximum lower sum, cannot make up
the difference of the RHS, the upper sum, as they need to sum to 0.

Bounds:
Combining n < (d_k + 1) a^k and d_k b^k <= 2n, we get 
d_k b^k < 2 (d_k + 1) a^k.
Rearranging, k < (log(2) + log((d_k+1)/d_k)) / log(b/a)
Assuming d_k >= 1 gives k < (2 log 2) / log(b/a)
If you use the weaker bounds b^k < 2 a^{k+1}, you get
k < log(2a) / log(b/a).

Also we have b < 3a. If b >= 3a, then 2 a^i - b^i <= -a for all i >= 1.
The i = 0 term is d_0 < a, so the overall sum is negative (if there are any 
nonzero higher digits).
"""

from math import log

def F(a, b):
    k = int(log(4) / log(b / a))

    # j = current power for d_j
    # t = target sum_{i=j+1..k} d_i (2 a^i - b^i)
    # l = bound on lower digits sum_{i=0..j} (a-1) |2 a^i - b^i|
    # n = result sum_{i=j+1..k} d_i a^i
    def f(j, t, l, n):
        if j == -1:
            return n if t == 0 else 0

        new_l = l - (a-1) * abs(2*a**j - b**j)

        for d in range(a-1, -1, -1):
            new_t = t + d * (2*a**j - b**j)
            if (new_l >= abs(new_t)):
                ret = f(j-1, new_t, new_l, n + d * a**j)
                if ret != 0: return ret

        return 0

    l = sum((a-1) * abs(2*a**i - b**i) for i in range(k+1))
    return f(k, 0, l, 0)

def G(a):
    return sum(F(a, b) for b in range(a+1, 3*a))

print(sum(G(a) for a in range(2, 21)))
