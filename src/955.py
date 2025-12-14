# Clearly, the diff between the triangle numbers are triangular themselves
# So given m-th triangle number T_m, find smallest T_k so that
# T_m + T_k = T_n, where T_n becomes the next triangular number
#
# Given m, solve m(m+1)/2 + k(k+1)/2 = n(n+1)/2
# Multiplying by 8 and completing the squares: 
# (trick from another paper about counting sums of triangles)
# 4m^2 + 4m + 1 + 4k^2 + 4k + 1 = 4n^2 + 4n + 1
# <=> (2m+1)^2 + (2k+1)^2 = (2n+1)^2 + 1
# Let m' = 2m+1, k' = 2k+1, n' = 2n+1 be odd integers
# <=> m'^2 + k'^2 = n'^2 + 1
# Since m' is given, we can rearrange as difference of squares
# m'^2 - 1 = n'^2 - k'^2 = (n'-k')(n'+k')
#
# Then all that's left is factor z = m'^2 - 1 as x * y
# (A shortcut is m'^2 - 1 also factors as diff of squares)
# (where n' = (y+x)/2, k' = (y-x)/2) and pick smallest k'
# then increment index by k for next iter

from number import divisors, factor

def f(N):
    m = 2  # start at T_m = 3
    ind = 0  # index of a_n

    for i in range(1, N+1):  # i-th triangle number
        print(f"{i} a({ind})={m*(m+1)//2}")
        if i == N: break
        mm = 2 * m + 1
        z = mm**2 - 1
        
        # most computational part
        f1, f2 = factor(mm - 1), factor(mm + 1)
        divs = divisors(f1 + f2)  # combine factor Counters
        best_kk = 0
        best_nn = 0
        
        for x in sorted(divs):
            y = z // x
            if x >= y: break
            # x and y must be same parity to get integer n' and k'
            # so x and y must be even because z = x * y is even
            if x % 2 == 0 and y % 2 == 0:
                nn = (x + y) // 2
                kk = (y - x) // 2
                # k' = 1 is trivial solution where m' = n'
                # also k' must be odd to get valid k
                if kk > 1 and kk % 2 == 1:
                    best_kk = kk
                    best_nn = nn
        
        n = (best_nn - 1) // 2
        k = (best_kk - 1) // 2
        ind += k
        m = n

    return ind

print(f(70))
