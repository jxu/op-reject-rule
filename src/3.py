x = 600851475143

def split(x): 
    for i in range(3, int(x**0.5)+1):
        if x % i == 0:
            return max(i, split(x//i)) # Small prime factored out
              
    return x
            
print(split(x))

    