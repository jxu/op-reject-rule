from sympy import n_order
M = 1234567891

def square_smallest(l):
    i = l.index(min(l))  # O(n), O(log n) with heap
    l[i] *= l[i]

def S(n, m):
    rounds = m
    l = list(range(2, n+1))
    while min(l)**2 < max(l):
        square_smallest(l)
        rounds -= 1
    l = sorted(l)

    print(l)
    print(rounds)
    rounds_all = rounds // (n-1)
    rounds_extra = rounds % (n-1)

    for i in range(n-1):
        x = l[i]
        ordx = n_order(x, M)
        #print(x, ordx)
        r = pow(2, rounds_all, ordx)
        l[i] = pow(x, r, M)

    for i in range(rounds_extra):
        l[i] = (l[i] ** 2) % M

    print(l)
    return sum(l) % M

print(S(10**4, 10**16))
