# Hidden points are coordinates (either one-dimensional or two-dimensional (x,y)) that are not coprime
# H(n) = 6(Sum[n - phi(n), {n, 1, 5}])
from number import totient_range # Until totient_sum fixed
def H(n): return 6*(n*(n+1)//2 - sum(totient_range(n)))
print(H(100000000))