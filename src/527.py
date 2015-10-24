# DP and memoization with dictionaries
# Binary: simple (A001855)

dict_limit = 100000
memo_B = {}

def B(L, H, x):
    #print(L, H, x)
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

#print(B(1, 6, 1))

memo_R = [0]*dict_limit

# STILL TOO SLOW!!
def R(L, H, x):
    if H < L: return 0
    if H == L: return x

    d = H - L
    if d < dict_limit and memo_R[d]:
        return memo_R[d]

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

    if d < dict_limit:
        memo_R[d] = r / (H - L + 1)

    return r / (H - L + 1)

print(R(1, 10000, 1))
print(memo_R)