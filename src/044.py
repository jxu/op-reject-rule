r = 5000
pent = [n*(3*n-1)//2 for n in range(1,r)]
ps = set(pent)

for j in range(r-1):
    for k in range(j):
        if pent[j] - pent[k] in ps and pent[j] + pent[k] in ps:
            print(pent[j] - pent[k])