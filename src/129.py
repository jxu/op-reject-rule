from fractions import gcd
def A(n):
    if gcd(n, 10) != 1: return 0
    x = 1
    k = 1
    while x:
        x = (x*10 + 1) % n  # 1, 11, 111, ... mod n
        k += 1

    return k

n = 1000001  # Guess A(n) < n
while True:
    if A(n) > 1000000:
        print(n)
        break
    n += 2
