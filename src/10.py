# Sieve
nums = [0] * 2000000
n = 0

for i in range(2, 2000000):
    if nums[i] == 0:
        n += i
        for j in range(2*i, 2000000, i):
            nums[j] = 1
            
print(n)
