def sieve(n):
    nums = [0] * n 
    for i in range(2, int(n**0.5)+1):
        if nums[i] == 0:
            for j in range(2*i, n, i):
                nums[j] = 1
    
    l = set()
    for i in range(2, n):
        if nums[i] == 0: l.add(i)
        
    return l
    

primes = sieve(1000)
max_p = 0
product = 0

for a in range(-999, 1000):
    for b in range(1000): # n=0, prime>0
        n = 0
        while True:
            if (n*n + a*n + b) not in primes: break
            n += 1
            
        if n > max_p:
            max_p = n
            product = a*b
            
print(product)

    

