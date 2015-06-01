# Hexagonal numbers are also triangular
P = set(n*(3*n-1)//2 for n in range(100000))
H = set(n*(2*n-1) for n in range(100000))

for h in H:
    if h>40755 and h in P:
        print(h)
        break