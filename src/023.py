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

def is_sum(n, nums):
    for a in nums:
        if n - a in nums: # O(1) for set
            return True
        
    return False
    
s = 0
for i in range(1, 28123):
    if not is_sum(i, set(abundant_nums)):
        s += i
        
print(s)