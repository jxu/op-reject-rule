

def Skew(T):
    mom1 = [1] * (T+1)
    mom1[0] = 0
    
    mom2 = [1] * (T+1)
    mom2[0] = 0
    mom3 = [1] * (T+1)
    mom3[0] = 0

    for t in range(2, T+1):
        mom2[t] = mom2[t-1] + mom2[t-2]
        mom3[t] = mom3[t-1] + 3 * mom3[t-2]

    print(mom2)
    print(mom3)
    # compute for T
    mu = 1
    var = mom2[T] - 1
    skew = (mom3[T] - 3 * var - 1) / (var ** (3/2))

    print(mu, var, skew)

    return skew

print(round(Skew(50), 8))
