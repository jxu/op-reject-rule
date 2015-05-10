def valid(n):
    for i in range(1, 21):
        if (n % i != 0): return False
    return True

n = 1
for i in range(1, 21):
    n *= i

for i in range(2, 21): # Factor out repeats
    if (n % i == 0) and valid(n // i):
        n //= i

print(n)
        
        
    