# Probability all stopped is (1-(1/2)^k)^n ~ log_2(n)
N = 0
i_prob = 1
k = 0
while i_prob > 10**-11:
    i_prob = 1 - (1-(1/2)**k)**32
    print(i_prob)
    N += i_prob
    k += 1

print(round(N, 10))