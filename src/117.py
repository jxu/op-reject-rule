memo = [0]*51

def F(n):
    if n < 0: return 0
    if n < 2: return 1
    if memo[n]: return memo[n]
    else:
        memo[n] = F(n-1) + F(n-2) + F(n-3) + F(n-4)
        return memo[n]

print(F(50))