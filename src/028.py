n = 1001
x = 1
s = 1

circles = n//2
for c in range(1, circles+1):
    for j in range(4): # 4 sides per revolution
        x += 2*c
        s += x
        
print(s)