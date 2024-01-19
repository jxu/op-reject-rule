# Working through examples, if a node is 2^k less its parent, then its
# children are -2^j from the node, for j < k. T_8:
#          -0
#    -1    -2    -4
#  -2  -4  -4
# -4
# So for difference d := n - k, Let n be the current node along the path.
# If d has bit 2^i set, then n -= 2^i
def f(n, k):
    d = n - k
    s = n
    for i in range(64):
        if (d >> i) & 1:
            n -= 1 << i
            s += n
    return s

print(f(10**17, 9**17))
