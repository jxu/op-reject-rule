from math import log

def F(a, b):
    k = int(log(4) / log(b / a))

    # j = current power for d_j
    # t = target sum_{i=j+1..k} d_i (2 a^i - b^i)
    # l = bound on lower digits sum_{i=0..j} (a-1) |2 a^i - b^i|
    # n = result sum_{i=j+1..k} d_i a^i
    def f(j, t, l, n):
        if j == -1:
            return n if t == 0 else 0

        new_l = l - (a-1) * abs(2*a**j - b**j)

        for d in range(a-1, -1, -1):
            new_t = t + d * (2*a**j - b**j)
            if (new_l >= abs(new_t)):
                ret = f(j-1, new_t, new_l, n + d * a**j)
                if ret != 0: return ret

        return 0

    l = sum((a-1) * abs(2*a**i - b**i) for i in range(k+1))
    return f(k, 0, l, 0)

def G(a):
    return sum(F(a, b) for b in range(a+1, 3*a))

print(sum(G(a) for a in range(2, 21)))
