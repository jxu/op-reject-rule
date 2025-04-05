# for r, b > 0: both red prob (r/(r+b)) * ((r-1)/(r-1+b)), return P(r-2,b)
# both black prob (b/(r+b)) * ((b-1)/(r+b-1)), return P(r,b)
# otherwise prob mixed is (2rb)/((r+b)(r+b-1)), return p(r, b-1)
# simple O(RB) DP is fast enough.
# (the project euler thread ofc found a closed form for P(2b,b) and P(r,b))

def P(R, B):
    a = [0]*(R+1)  # DP, init P(R, 0) = 0

    for b in range(1, B+1):
        a[0] = 1  # P(0, B) = 1
        # overwrite row B-1 with B to only use O(B) storage in python
        for r in range(2, R+1, 2):  # only ever use even r
            #  a[r-2] = P(r-2, B), old a[r] = P(R, B-1)
            d = (r+b)*(r+b-1)
            a[r] = (r*(r-1)*a[r-2] + 2*r*b*a[r]) / d / (1 - (b*(b-1))/d)

    return a[R]

print(round(P(24690,12345), 10))
