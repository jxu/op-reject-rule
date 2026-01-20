# Compute using (non-central) moments E[X], E[X^2], E[X^3]
# See notebook for computing recurrences

def Skew(T):
    mom2 = [0] * (T+1)
    mom2[1] = 1
    mom3 = [0] * (T+1)
    mom3[1] = 1

    for t in range(2, T+1):
        mom2[t] = mom2[t-1] + mom2[t-2]
        mom3[t] = mom3[t-1] + 3 * mom3[t-2]

    var = mom2[T] - 1
    skew = (mom3[T] - 3 * var - 1) / (var ** (3/2))
    return skew

print(round(Skew(50), 8))
