chain_lens = [0]*1000000
max_len = 0
max_i = 0

for i in range(1, 1000000):
    current_len = 1
    n = i
    
    while (n != 1):
        if (n % 2 == 0):
            n //= 2
        else:
            n = 3*n + 1
    
        if n < 1000000 and chain_lens[n] != 0: # Prev chain memoized
            current_len += chain_lens[n]
            break
        else:
            current_len += 1
        
    chain_lens[i] = current_len 
    if current_len > max_len:
        max_len = current_len
        max_i = i
 
print(max_i, max_len)
        
