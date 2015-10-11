memo = [[0]*51 for i in range(5)]

def F(m, n):
    if n < m: return 1
    if memo[m][n]: return memo[m][n]
    else:
        memo[m][n] = F(m, n-1) + F(m, n-m)
        return F(m, n-1) + F(m, n-m)

print(F(2, 50) + F(3, 50) + F(4, 50) - 3)  # Exclude 3 empty solutions