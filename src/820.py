# Find repeating decimal digits via long division and checking remainders

def d(n, k):
    rems = []
    qs = []
    rem = 1
    rep_i = 0
    for i in range(10):
        d = rem * 10
        q = d // k
        #print(d, q, rem, rems, qs)

        try:
            rep_i = rems.index(rem)
            #print(rep_i, rem, rems, qs)
            break
        except: pass

        rems.append(rem)
        qs.append(q)
        rem = d - k * q

    print(rep_i, rems, qs)
    dec_start = qs[:rep_i]
    repetend = qs[rep_i:]

    print(dec_start, repetend)
    idx = (n - 1 - len(dec_start)) % len(repetend)
    return repetend[idx]

print(d(4,4))

def S(n):
    return sum(d(n,k) for k in range(1,n+1))

#print(S(100))