from sympy.ntheory import factorint

def G(n):
    for c in range(n):
        x = n - c*(c+1)//2
        if x < 1: return
        print(x, factorint(x))

G(17526 * 10**9)