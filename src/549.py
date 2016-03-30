# Kempner numbers
from fractions import gcd

def S(n):
    n_list = [x for x in range(n+1)]
    s_list = [0]*(n+1)

    for m in range(1, n+1):
        for i in range(2, n+1):
            if s_list[i] == 0:
                n_list[i] //= gcd(m, n_list[i])
                if n_list[i] == 1: s_list[i] = m

        #print(n_list)
    #print(s_list)
    return sum(s_list[2:])



print(S(100))