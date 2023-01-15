from number import comb
def A(k, n):
    s = 0
    for i in range(0, k//2+1):
        t = comb(k,i) * comb(k-i,i) * (2**((k-2*i)*(n//k)))
        print(t)
        s += t

    return s

print(A(4,20))