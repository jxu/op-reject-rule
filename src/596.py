
def tri(n):
    return n * (n+1) // 2

# A024916
def sum_sigma(n):
    c = int(n**0.5)
    s = 0
    for i in range(1, c+1):
        s += i * (n // i)
    for j in range(1, c+1):
        s += tri(n // j)
    s -= tri(c) * c
    return s


def T(r):
    return 8 * (sum_sigma(r**2) - 4 * sum_sigma(r**2 // 4)) + 1

print(T(10**8) % (10**9 + 7))
