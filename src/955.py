from number import divisors, factor

m = 2
ind = 0

for i in range(1, 71):
    print("i m Tm ind", i, m, m*(m+1)//2, ind)
    mm = 2 * m + 1
    x = mm**2 - 1
    
    pp = factor(x)
    print(pp)
    divs = sorted(divisors(pp))
    best_kk = None
    best_nn = None
    
    for d in divs:
        if d*d >= x: break
        y = x // d
        if d % 2 == 0 and y % 2 == 0 and ((y - d) // 2) > 1:
            nn = (d + y) // 2
            kk = (y - d) // 2
            if kk > 1 and kk % 2 == 1:
                best_kk = kk
                best_nn = nn

    
    n = (best_nn - 1) // 2
    k = (best_kk - 1) // 2
    #print("n", n, k)
    m = n

    ind += k
