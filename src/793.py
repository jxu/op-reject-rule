# Let ord(m) be # pairs SiSj < m.
# For odd n, median is (least) m with ord(m) = (n choose 2) // 2.
# Sort S. Binary search m:
# For each i, binary search max j s.t. SiSj < m.
# Then ord(m) = sum over (i,j) of j-i or 0
# Time complexity O(n log n log M) where M is max product

# Original over-complicated idea: median minimizes absolute error
# median = argmin_m sum_{i<j} |SiSj - m| = argmin_m sum_{i!=j} |SiSj - m|
# Ternary search m:
# For each i, binary search max j* s.t. SiSj* < m
# Sum over |SiSj - m| with two cases, j < j* and j >= j*
# Using prefix sums for Sj, ex. for j < j*,
# sum_{i!=j,j<j*} |SiSj - m| = (j* - [i<j*])*m - Si sum_{i!=j,j<j*} Sj

def binary_search(f, l, r):
    while r - l > 1:
        m = (l + r) // 2
        if f(m): r = m
        else: l = m
    return l

def ord(m):
    s = 0
    for i in range(n):
        j = binary_search(lambda j: S[i]*S[j] >= m, -1, n)
        s += max(j-i, 0)
    print("ord", m, s)
    return s

n = 1000003
mod = 50515093
s = 290797
S = []
for i in range(n):
    S.append(s)
    s = (s**2) % mod

S.sort()
med = (n * (n-1) // 2) // 2
print(binary_search(lambda m: ord(m) > med, 0, mod ** 2))