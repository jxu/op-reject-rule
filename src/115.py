# F(m, n) = F(m, n-1) + F(m, n-m-1) + F(m, n-m-2) + ... + F(m, -1)
def F(m, n):
    if n < m: return 1

    s = F(m, n-1)
    for i in range(n-1-m, -2, -1):
        s += F(m, i)
    return s

n = 51
while F(50, n) <= 1000000:
    n += 1
print(n, F(50,n))
