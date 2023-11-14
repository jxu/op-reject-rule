
def R(n):
    e = [0] * n

    for t in range(50):
        for i in range(1, n):
            best_x = 1e9
            for a in range(3):
                for b in range(3):
                    if a == b == 0: continue
                    y = i * 5**a * 6**b
                    z = (y % n) / y * e[y % n] + a + b
                    best_x = min(best_x, z)
            e[i] = best_x
    return e[1]

def S(n):
    return sum(R(k) for k in range(2, n+1))

print(round(S(1000), 6))