"""Well Drilling

Recurrence (expected drilling time if already drilled to x)
f(x) = min_{y>x} (y + e^(x-y) f(y)) 
cond prob of not finding water drilling to y, given drilled to x, = e^-y / e^-x

I couldn't figure out how to solve this recurrence, because f(x) depends on
every possible value of f(y). However, if we knew the optimal sequence
x0 < x1 < x2 < ... (with x0 = 0), the expected value would be 
= x1 + e^-x1 (x2 + e^(-x2+x1)(x3 + ...))
= e^-x0 x1 + e^-x1 x2 + e^-x2 x3 + ...
interestingly due to the memoryless property P(X > x + k | X > k) = P(X > x)

To solve, I set x0 = 0, x_N = large depth, and iteratively solve coordinates
based on partial derivative* 
0 = df / dx_i = e^(-x_{i-1}) - e^(-x_i) x_{i+1}
=> x_i = x_{i-1} + log(x_{i+1})

*I believe this is coordinate descent, as gradient 0 <=> partial derivatives 0

I fixed x_N to be large as I thought the values would all tend to 0 if there
was no way to force a deep drill for big N. 
From the solution thread, I just got lucky with my x_1 starting value. 
Too small and it would've converged to a local minimum. 
"""

from math import exp, log

x = list(range(100)) + [1000]

for l in range(100):
    for i in range(1, len(x)-1):
        x[i] = x[i-1] + log(x[i+1])

    d = 0
    for i in range(1, len(x)):
        d += exp(-x[i-1]) * x[i]

    print(d)

print(x)
print(round(d, 9))
