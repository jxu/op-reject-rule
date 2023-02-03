# 8^12 * 12^8 = 3^8 * 2^52
# XOR-product corresponds to polynomial multiplication in Z_2[x]
# Compute XOR-power for 3^8, then use "freshman's dream" where
# (x^3 + x + 1)^2 = (x^3)^2 + (x)^2 + 1^2 in Z_2[x] and so forth
# at the end, to return to binary numbers, evaluate polynomial at x=2
M = 10**9 + 7

def xor_product(x, y):
    r = 0
    while y:
        if y & 1:
            r ^= x
        x <<= 1
        y >>= 1
    return r

r = 1
for i in range(3**8):
    r = xor_product(r, 11)

s = 0
for i in range(3**9+1):
    if (r >> i) & 1:
        s = (s + pow(2, i * 2**52, M)) % M

print(s)