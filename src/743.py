from number import comb, sieve, mul_inv
M = 1000000007

fact = [1] * (10**8 + 1)
x = 1
for i in range(1, 10**8 + 1):
    fact[i] = (fact[i-1] * i) % M

def A(k, n):
    s = 0
    for i in range(0, k//2+1):
        t = (fact[k] * mul_inv(fact[i] * fact[k-i], M)) % M * \
            (fact[k-i] * mul_inv(fact[i] * fact[k-2*i], M)) % M * \
            pow(2, (k-2*i)*(n//k), M)
        s = (s + t) % M

    return s

print(A(10**8, 10**16))