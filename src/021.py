def sum_factors(n):
    s = 0
    for i in range(2, int(n**0.5)+1):
        if (n % i == 0):
            if (n//i == i): s += i # Square
            else: s += n//i + i
            
    return s + 1 # 1 as factor

l = [sum_factors(n) for n in range(10000)]

s = 0
for i in range(10000):
    if l[i] < 10000 and l[l[i]] == i and l[i] != i:
        s += i
        
print(s)
        

        