# Euler's theorem: a^phi(n) = 1 mod n  --> periods of 2^n
# 2^x mod 14^8 = 2^8 (2^(x-8) mod 7^8), period phi(7^8) = 4941258

period = 4941258

def pow_2_mod(n):
    if n < 8:
        return pow(2, n)
    else:
        return pow(2, n % 4941258, 14**8)

def pow_pow_2_mod(n):
    return pow(2, pow(2, n, period), 14**8)




def ackermann(m, n):

    if m <= 3 and n <= 3:
        return ((1, 2, 3, 4), (2, 3, 4, 5), (3, 5, 7, 9), (5, 13, 29, 61))[m][n]
    if m == 3: return (pow_2_mod(n+3) - 3) % 14**8


    A = ackermann
    z = pow(2, period, 14**8)
    if (m, n) == (4, 4):
        #y = pow(2, 2**65536, period)
        y = pow_pow_2_mod(65536)
        return (z * 2**y - 3) % 14**8


print(ackermann(4, 4))


