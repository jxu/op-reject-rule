from fractions import gcd
s = 0
for d in range(12001):
    for n in range(int(d/3)+1, int(d/2)+1):
        if 2*n != d and gcd(n, d) == 1:
            s += 1

print(s)