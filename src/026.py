# Period = smallest k such that d divides 10^k - 1
max_p = 0
max_d = 0
for d in range(2, 1000):
    if d % 2 != 0 and d %5 != 0:
        for k in range(1, 1000):
            if (10**k - 1) % d == 0:
                if k > max_p:
                    max_p = k
                    max_d = d
                break
    
print(max_d)
