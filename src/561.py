# a = 2^x_1 + 3^x_2 + 5^x_3 + 7^x_4 + ...  b = 2^y_1 + 3^y_2 + 5^y_3 + 7^y_4 + ...
# Number of pairs is number of prime exponent pairs 0 <= x_1 <= y_1 <= n, etc.
# Also, (x_1, x_2, ...) != (y_1, y_2, ...) so a and b are distinct
# S((p_m#)^n) = ((n+1)(n+2)/2)^m - (n+1)^m

def E_test(m, n):
    r = pow((n+1)*(n+2)//2, m, 2**100) - pow(n+1, m, 2**100)
    E = 0
    while r%2 == 0:
        r //= 2
        E += 1
    print(E, end='\t')
    if n%4 == 3: print()

print('\t', end='')
for n in range(1, 101):
    E_test(16, n)