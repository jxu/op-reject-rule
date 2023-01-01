# Let sorted list be a_1 <= ... <= a_n' (where n' = n-1)
# After a few rounds, a_1^2 will be at least a_n'
# Squaring the inequality implies a_1^2 <= ... <= a_n'^2
# When a_1^2 >= a_n', all squares end up >= a_n', so each value gets squared
# once every n' rounds.
# So subtract off rounds until a_1^2 >= a_n', square each elem (rounds // n')
# times, then finally square the remaining smallest (rounds % n') elems.

# For elem x, to square k (~10^12) times we compute x^(2^k) mod 1234567891.
# Mul order of x divides phi(1234567891) = 1234567890, so x's exponent is only
# 2^k mod 1234567890

M = 1234567891

def S(n, m):
    rounds = m
    l = list(range(2, n+1))
    while min(l)**2 < max(l):
        # square smallest
        i = l.index(min(l))  # O(n), O(log n) with heap
        l[i] *= l[i]
        rounds -= 1
    l = sorted(l)

    print(l)
    print(rounds)
    rounds_all = rounds // (n-1)
    rounds_extra = rounds % (n-1)

    for i in range(n-1):
        r = pow(2, rounds_all, M-1)
        l[i] = pow(l[i], r, M)

    for i in range(rounds_extra):
        l[i] = (l[i] ** 2) % M

    return sum(l) % M

print(S(10**4, 10**16))
