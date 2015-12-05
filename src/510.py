# d = ab / (2*sqrt(ab) + a + b)
def S(n):
    #squares = set(x*x for x in range(n+1))
    # a = b = 4*c, sum 4*c + 4*c + c
    z = n // 4
    s = 9 * z * (z+1) // 2

    # The rest: Values of a, b such that ab is square and d is integer

    for a in range(1, 1000):
        for b in range(1, a):
            if a*b % (a + b + 2*(a*b)**0.5) == 0:
                print(a, b)



    return s

print(S(100))
