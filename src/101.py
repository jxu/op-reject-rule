def u(n): return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

def lazy():
    from scipy import interpolate

    x = list(range(1, 11))
    y = [u(n) for n in range(1, 11)]

    FITs = 0
    for d in range(1, 11):
        z = interpolate.lagrange(x[:d], y[:d])
        FITs += round(z(d+1))

    return FITs


def FIT(k):
    # Lagrange polynomial interpolation
    L = 0
    for j in range(1, k+1):
        s = u(j)
        for m in range(1, k+1):
            if m != j:
                s *= (k+1 - m) / (j - m)

        L += s
    return L

print(round(sum(FIT(n) for n in range(1, 11))))
