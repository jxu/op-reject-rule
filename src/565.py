# Divisor sum function = sigma(n) = ((p_1^(a_1+1) - 1) / (p_1 - 1))*((p_2^(a_2+1) - 1) / (p_2 - 1))*...
# Current method: at least one of these factors must be a multiple of 2017
# For each p_1 and a_1, sum multiples of p_1^a_1, not divisible by p_1^(a_1+1) (then a_1 is different)
# Implement sigma efficiently later in number.py?
from number import sieve, is_prime

def S(n, d):
    s = 0
    # Test first factor (p^2-1)/(p-1) = p+1, so d|p+1, p < 10^11
    for f in range(2*d, n, 2*d):  # Test even f
        if is_prime(f-1):
            if (f-1)%1000 == 727: print(f-1, 1)

            # Multiples of f-1
            pass

    # Test rest of factors
    primes = sieve(int(n**0.5)+1)
    for a_1 in range(2, 40):
        for p_1 in primes:
            if p_1 < n**(1/a_1):
                if (p_1**(a_1+1)-1)//(p_1-1) % d == 0:
                    print(p_1, a_1)
                    #x = n // p_1**a_1
                    #y = n // (p_1**(a_1+1)) - 1
                    #print(p_1**a_1, x, y)
                    #s += p_1**a_1 * ((x+1)*x//2 - (p_1*y+1)*p_1*y//2)
                    #print(s)


#print(S(20, 7))
#print(S(10**11, 2017))

def f_test():
    l = []
    for p in sieve(100):
        for a in range(1, 11):
            x = (p**(a+1)-1)//(p-1)
            print(x, p, a)
            if x in l: print(x)
            l.append(x)

f_test()