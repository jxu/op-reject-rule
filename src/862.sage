"""
The combinatorics solution is using exponential generating functions
For a string with c0 0s, c1 1s, etc. the number of permutations for each
equivalence class O is the multinomial |O| = k! / (c0!c1!...c9!)
For each O, contribute O + 1 + ... + (|O| - 1) = (|O|^2 - |O|)/2 to sum

The EGF where [x^k/k!] counts the sum of all |O| is
(x^0/0! + x^1/1! + ...)^10 = e^(10x)
Where each series term represents picking ci of digit i.

To count sum of all |O|^2, just square the coefficients:
(x^0/(0!^2) + x^1/(1!^2) + ...)^10

To handle excluding leading zeros, observe c0/k of the permutations have a
leading zero. Therefore the first series, representing c0, is modified as
(1-0/k) x^0/0! + (1-1/k)x^1/1! + ... = (1-x/k) e^x
Similar for the squared terms. The final result is (w2-w1)/2, where
w1 = [x^k/k!](1-x/k)e^(10x) = 9 * 10^(k-1)
w2 = [x^k/k!^2] (sum_i=0..inf (1-i/k)^2 x^i/i!^2) (sum_i=0..inf x^i/i!^2)^9
"""

k = 12

R.<x> = PowerSeriesRing(QQ, default_prec=k+1)

# EGF[1 - i/k, i, x]
g1a = sum((1 - i/k) * x^i / factorial(i) for i in range(k+1))

# EGF[1, n, x]^9
g1b = exp(x)^9

g1 = (g1a * g1b).truncate(k+1)


# Sum[x^i ((1-i/k)/i!)^2, i=0..∞]
a = sum(
    ((1 - i/k) / factorial(i))^2 * x^i
    for i in range(k+1)
)

# GeneratingFunction[(1/n!)^2, n, x]
b = sum(
    x^n / factorial(n)^2
    for n in range(k+1)
)

g2 = (a * b^9).truncate(k+1)


result = ((factorial(k)^2 * g2 - factorial(k) * g1) / 2)[k]

result