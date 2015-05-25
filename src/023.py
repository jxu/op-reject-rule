def is_abundant(n):
    s = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if n//i == i: s += i
            else: s += i + n//i
    
    return s + 1 > n

abundant_nums = []
for i in range(1, 28123):
    if is_abundant(i): abundant_nums.append(i)
    
print(abundant_nums)

sums = [0]*28123

for a in range(len(abundant_nums)):
    for b in range(a, len(abundant_nums)):
        x = abundant_nums[a] + abundant_nums[b]
        if x >= 28123: break
        sums[x] = 1
        
s = 0
for n in range(len(sums)):
    if sums[n] == 0: s += n
    
print(s)