memo = {}

def knuth_arrow(a, n, b, m):
    if (a, n, b) in memo:
        return memo[(a, n, b)]

    if n == 0:
        return (a*b) % m

    if n == 1:
        s = pow(a, b, m)
        memo[(a, n, b)] = s
        return s

    if n > 1:
        s = a
        for i in range(b-1):
            s = knuth_arrow(a, n-1, s, m)

        memo[(a, n, b)] = s
        return s


def ackermann(m, n, mod):
    if (m, n) == (0, 0): return 1
    if (m, n) == (1, 1): return 3
    return knuth_arrow(2, m-2, n+3, mod) - 3

print(ackermann(5, 5, 14**8))

