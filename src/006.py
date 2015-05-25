a = b = 0
for i in range(101):
    a += i
    b += i**2
    
print(a**2 - b)
    
# One-liner
print(sum(range(101))**2 - sum(i*i for i in range(101)))
