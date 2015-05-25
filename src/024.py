# Permutations: n! = n * (n-1)!
# P9 = d + [remaining]
import math

s = ""
nums_left = list(range(10))
n = 10**6 - 1 # Millionth zero-indexed :P

for i in range(10, 0, -1):
    x = n // math.factorial(i-1) # Multiples of (i-1)! to right
    s += str(nums_left[x]) # nth digit avaiable to use
    nums_left.remove(nums_left[x])
    n = n % math.factorial(i-1)
    print(s)
    
    
