"""New solution

For each fixed t, gcd(a, b) = 2^t <=> gcd(a/2^t, b/2^t) = 1 
So for each b (div by 2^t), the # a's satisfying is phi(b/2^t)
For a < b <= N, this is summatory function Phi(b / 2^t)
The exception is when b/2^t = 1, where we want phi(1) = 0 instead of 1 

See 643ie for original solution
"""

from number import totient_sum

N = 10**11

s = 0
p2 = 2 
while p2 <= N:
    s += totient_sum(N // p2) - 1 
    p2 *= 2
    
print(s % 1000000007)
