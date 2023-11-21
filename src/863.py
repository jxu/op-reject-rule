
def R(n):
    e = [0] * n
    for t in range(50):
        for i in range(1, n):
            e[i] = 1 + min(5*i%n/(5*i) * e[5*i%n],
                           6*i%n/(6*i) * e[6*i%n])
    return e[1]

def S(n):
    return sum(R(k) for k in range(2, n+1))

print(round(S(1000), 6))