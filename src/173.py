def llama(N):
    llamas = 0
    pad = 2
    while (1 + pad)**2 - 1 <= N:
        x = 1
        while (x + pad)**2 - x**2 <= N:
            llamas += 1
            x += 1
                
        pad += 2
    return llamas
        
print(llama(1000000))
