a = b = c = 1
n = 0
while (c < 4000000):
    if (c % 2 == 0): n += c
    c = a + b
    a = b
    b = c
    
print(n)
    

