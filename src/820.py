# Determine nth decimal digit directly: from long division, by subtracting out
# multiples of k, nth (0-index) remainder is 10^n mod k

def d(n, k):
    rem = pow(10, n-1, k)
    q = 10 * rem // k
    return q

def S(n):
    return sum(d(n,k) for k in range(1,n+1))

print(S(10**7))

# one-liner
n = 10**7; print(sum((10 * pow(10, n-1, k)) // k for k in range(1,n+1)))