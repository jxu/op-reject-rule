from number import combination
print(sum(combination(n, r) > 10**6 for n in range(1, 101) for r in range(n+1)))