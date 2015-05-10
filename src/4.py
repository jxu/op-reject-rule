n = 0
for i in range(999, 100, -1):
    for j in range(i, 100, -1):
        s = str(i*j)
        if (s[::-1] == s): n = max(n, i*j)
        
print(n)
            
        

        