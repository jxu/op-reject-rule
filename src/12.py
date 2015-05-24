# n = p^v_1 * p^v_2 * ...
# d = (v_1 + 1)(v_2 + 1)...
i = 2
n = 1
total_factors = -1
while not total_factors > 500:
    n += i
    i += 1

    m = n
    # Factor list not necessary, possible to only keep track of one factor at a time
    factor_list = [] 
    while (m != 1):
        for p in range(2, m+1):
            if (m % p == 0):
                m //= p
                factor_list.append(p)
                break
                
    factor_count = [factor_list.count(i) for i in set(factor_list)]
    
    total_factors = 1
    for f in factor_count:
        total_factors *= f + 1

print(factor_list)
print(n)
        

    
    