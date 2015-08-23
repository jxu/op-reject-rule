from number import sieve
primes = sieve(100)

def this_again(min_start, current, target_sum):
    if current == target_sum:
        return 1
    
    s = 0
    if current < target_sum:   
        for p in primes:
            if min_start <= p:
                s += this_again(p, current+p, target_sum)
                
    return s
            
for i in range(100):
    if this_again(0, 0, i) > 5000:
        print(i)
        break
