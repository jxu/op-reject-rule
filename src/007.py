# Sieve of Eratosthenes
nums = [0] * 200000
n = 0

for i in range(2, 200000):
    if nums[i] == 0:
        print(i)
        n += 1
        if n == 10001:
            break
        for j in range(2*i, 200000, i):
            nums[j] = 1
        
        
        
    