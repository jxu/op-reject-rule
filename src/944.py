M = 1234567891

def T(n): return n*(n+1)//2

def S(n):
    c = int(n**0.5)
    return ((T(n) * pow(2, n-1, M)) % M 
        - sum((i * pow(2, n - n//i, M)) % M for i in range(1, n//c + 1)) 
        - sum(((T(n//j) - T(n//(j+1))) * pow(2, n-j, M)) % M for j in range(1, c))) % M

print(S(10**14))
