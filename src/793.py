# testing median idea
n = 103
M = 50515093
s = [290797]
for i in range(n-1):
    s.append(pow(s[-1], 2, M))

ss = []
for i in range(n):
    for j in range(i+1, n):
       ss.append(s[i] * s[j])


def ternary_search(f, l, r):
    for i in range(100):
        print(l, r)
        m1 = l + (r-l) // 3
        m2 = r - (r-l) // 3
        if f(m1) < f(m2):
            r = m2
        else:
            l = m1
    return (l + r) // 2


def sae(m):
    return sum(abs(m-x) for x in ss)

print(ternary_search(sae, 0, M**2))
