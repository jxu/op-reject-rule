# only compute/store odd totients

def totient_range(n):
    def calc(i):
        if i <= 0: raise ValueError
        ih = i // 2
        if i % 2: return t[i // 2]
        else: return t[ih // 2] if ih % 2 else 2 * calc(ih)

    t = list(range(1, n + 1, 2))
    for p in range(3, n + 1, 2):
        if p == t[p // 2]:
            for k in range(p, n + 1, 2 * p):
                t[k // 2] -= t[k // 2] // p

    tots = list(calc(i) for i in range(1, n+1))

    return tots


print(totient_range(10))