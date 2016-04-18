# Cyclic number (10^(p-1)-1)/p = 00000000137...56789
# p*56789 = ...99999, p = ...09891
from number import is_prime

def starts137(p):
    return str((10**30 - 1) / p)[:3] == "137"  # Approximate 999... / p


for p in range(9891, 10**10, 100000):
    if(is_prime(p)) and starts137(p):
        print(p)






