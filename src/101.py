from scipy import interpolate

def u(n): return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

FITs = 0
x = list(range(1, 11))
y = [u(n) for n in range(1, 11)]
for d in range(10):
    z = interpolate.lagrange(x[:d+1], y[:d+1])
    FITs += round(z(d+2))

print(FITs)
