"""
The combinatorics solution is using exponential generating functions
For a string with c0 0s, c1 1s, etc. the number of permutations for each
equivalence class O is the multinomial |O| = k! / (c0! c1! ... c9!)
Each class contributes O + 1 + ... + (|O| - 1) = (|O|^2 - |O|)/2 to sum

The EGF where [x^k/k!] counts the sum of all |O| is
(x^0/0! + x^1/1! + ...)^10 = e^(10x)
Where each series term represents picking ci # of digit i.

To handle excluding leading zeros, observe c0/k of the permutations have a
leading zero. Therefore the first factor, representing c0, is scaled (1 - i/k) 
as in
sum_{i >= 0} (1 - i/k) x^i / i! = (1 - x/k) e^x

The kth EGF coef of (1 - x/k) e^x e^(9x) = 9 * 10^(k-1)
This has an intuitive interpretation for sum |O|: 9/10 perms don't have lead 0

Now |O|^2 = (k! / (c0! c1! ... c9!))^2
I figured I can just square the coefficients, and use
[x^k / k!^2] (sum_{i >= 0} x^i / i!^2)^10
(Apparently sum_{i >= 0} x^i / i!^2 is I0(2 sqrt x), modified Bessel function 
of the first kind)

To adjust for leading 0, we can scale the first factor by (1 - i/k)^2.
This doesn't have an easy closed form either.

The final result is (w2 - w1) / 2, where
w1 = 9 * 10^(k-1)
G0 = sum_{i >= 0} (1 - i/k)^2 x^i / i!^2
G = sum_{i >= 0} x^i / i!^2
w2 = [x^k/k!^2] G0 * G^9
"""

k = 12
R.<x> = PowerSeriesRing(QQ, default_prec=k+1)

# Sum[x^i ((1-i/k)/i!)^2, i=0..∞]
G0 = sum((1 - i/k)^2 * x^i / (factorial(i))^2 for i in range(k+1))

# GeneratingFunction[(1/n!)^2, n, x]
G = sum(x^n / factorial(n)^2 for n in range(k+1))

w1 = 9 * 10^(k-1)
w2 = factorial(k)^2 * (G0 * G^9)[k]
print((w2 - w1) / 2)
