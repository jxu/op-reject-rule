# Let sorted list be a_1 <= ... <= a_n' (where n' = n-1)
# After n rounds (idea from sol thread), a_1^2 will be at least a_n'
# Squaring the inequality implies a_1^2 <= ... <= a_n'^2
# When a_1^2 >= a_n', all squares end up >= a_n', so each value gets squared
# once every n' rounds.
# Square each elem (m-n)/n' times (where n' divides m-n)

# For elem x, to square k (~10^12) times we compute x^(2^k) mod 1234567891.
# Mul order of x divides phi(1234567891) = 1234567890, so x's exponent is only
# 2^k mod 1234567890

M = 1234567891

def S(n, m):
    n1 = n-1
    l = list(range(2, n+1))
    for j in range(n):
        # square smallest
        i = l.index(min(l))  # O(n), O(log n) with heap
        l[i] *= l[i]

    assert (m - n) % n1 == 0
    rounds_all = (m - n) // n1

    for i in range(n1):
        r = pow(2, rounds_all, M-1)
        l[i] = pow(l[i], r, M)

    return sum(l) % M

print(S(10**4, 10**16))
