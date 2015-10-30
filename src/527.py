 # Binary: DP and memoization with dictionaries (related A001855)
# Random: 1, 3/2, 17/9, 53/24, 62/25, ...
# numerator: A093418 denominator: A096620, given by -3n + 2(1+n)*HarmonicNumber(n))
import math

dict_limit = 100000
memo_B = {}

def B(L, H, x):
    if H < L: return 0
    if H == L: return x

    d = H - L
    if d < dict_limit and d in memo_B:
        return memo_B[d]
    g = (L + H) // 2
    r = x + B(L, g-1, x+1) + B(g+1, H, x+1)
    if d < dict_limit:
        memo_B[d] = r
    return r

# Test small cases
def R(L, H, x):
    if H < L: return 0
    if H == L: return x

    g_mid = (L + H) // 2
    g1 = g_mid
    g2 = g1 + 1
    r = 0
    while g1 >= L:
        r += x + R(L, g1-1, x+1) + R(g1+1, H, x+1)
        g1 -= 1

    while g2 <= H:
        r += x + R(L, g2-1, x+1) + R(g2+1, H, x+1)
        g2 += 1

    return r / (H - L + 1)


def harmonic(n):
    em = 0.57721566490153286060
    return em + math.log(n)


def R_shortcut(n):  # OEIS
    return -3*n + 2*(1+n)*harmonic(n)

b = B(1, 10**10, 1) / 10**10
r = R_shortcut(10**10) / 10**10
print(r, b, round(r-b, 8))
