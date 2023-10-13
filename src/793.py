# testing median idea
from itertools import accumulate
from bisect import bisect_left
from functools import cache

n = 1000003
M = 50515093
S = [290797]
for i in range(n-1):
    S.append(pow(S[-1], 2, M))

S.sort()
#S = [1, 2, 3]
print(S)
pre = [0] + list(accumulate(S))  # pre[i] is sum index < i
print(pre)


def ternary_search(f, l, r):
    for i in range(100):
        m1 = l + (r-l) // 3
        m2 = r - (r-l) // 3
        print(l, m1, m2, r)

        if f(m1) < f(m2):
            r = m2
        else:
            l = m1
    return (l + r) // 2

@cache
def sae(m):
    s = 0
    print(f"sae({m})")
    for i in range(n):
        js = bisect_left(S, m/S[i])
        #print(f"S[{i}] = {S[i]} S[j*{js}]",m/S[i])

        # y1 = 0
        # for j in range(0, js):
        #     if j == i: continue
        #     y1 += m - S[i]*S[j]

        y1 = (js - (i < js)) * m - S[i] * (pre[js] - (i < js) * S[i])

        y2 = S[i]*(pre[n] - pre[js] - (js <= i)*S[i]) - m * (n - js - (js <= i))
        # y2 = 0
        # for j in range(js, n):
        #     if i == j: continue
        #     y2 += S[i]*S[j] - m

        #print(y1, y2)

        s += y1 + y2

    return s

print(ternary_search(sae, 0, M**2))
#print(sae(4))