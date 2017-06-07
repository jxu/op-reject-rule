# Consider the coin toss rounds as a string of left or right winners
# Have the players in a line. Ex. 1 2 3 1 2 3
# A game is won and a string terminates if it ends in RL (same player won twice)

# For example take P_3(1). The first way to win is a string XXRL
# 1st X between 1 and 2, 2nd X between 2 and 3, R between 3 and 1, L between 1 and 2
# XX could be LL, LR, RR
# For string XXXXXRL: XXXXX could be LLLLL, LLLLR, LLLRR, LLRRR, LRRRR, RRRRR (num Xs + 1)
# So P_3(1) = 3*2^-4 + 6*2^-7 + 9*2^10 + ...

# General formula for P_n(k) = (k-1)*2^-k + (k-1+n)*2^(-k-n) + (k-1+2n)*2^(-k-2n) + ...
# = 2^-k * ((k-1)(2^0 + 2^-n + ...) + n*(2^-n + 2*2^-2n + 3*2^-3n + ...))
# ... some geometric series later ...
# = (((2^n - 1)(k - 1) + n) * 2^(n-k)) / (2^n - 1)^2

# Now hope it's reduced (which it is!)

def P(n, k):
    num = pow(2, n-k, 10**8) * ((pow(2, n, 10**8)-1)*(k-1) + n)
    den = (pow(2, n, 10**8) - 1)**2
    return (num % 10**8, den % 10**8)

x = P(10**8 + 7, 10**4 + 7)
print((x[0] * x[1]) % 10**8)
