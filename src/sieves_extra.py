def sieve_factor(n):
    fact = [[] for _ in range(n)]
    for i in range(2, n):
        if fact[i] == []:
            j = i
            while j <= n:
                for k in range(j, n, j):
                    fact[k].append(i)
                j *= i

    return fact

print(sieve_factor(11))