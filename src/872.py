# Working through examples, if a node is 2^k less its parent, then its
# children are -2^j from the node, for j < k. T_8:
#          -0
#    -1    -2    -4
#  -2  -4  -4
# -4
# So for difference d := n - k, Let n be the current node along the path.
# If d has bit 2^i set, then n -= 2^i
def f(n, k):
    # one-liner replacing d is confusing due to changing n
    d = n - k
    return n + sum(n := n - (1 << i) for i in range(64) if (d >> i) & 1)


def f2(n, k):
    # without assignment expression, because the nodes along the way are just
    # the first ith bits of d
    d = n - k
    mask = lambda i: (2 << i) - 1
    # can also use set to avoid conditional, since for the zero bits in d,
    # d & mask is the same (credit: hkmt)
    return n + sum(n - (d & mask(i)) for i in range(64) if (d >> i) & 1)

print(f(10**17, 9**17))
print(f2(10**17, 9**17))