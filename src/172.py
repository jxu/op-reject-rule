# simple DP and multinomial coefficient, with 1/10 numbers having leading zero
from number import multinomial

# yields m-tuples that sum to n
def dp(n, m):
    if m == 0:
        if n == 0:
            yield ()
        return 

    for k in range(4):
        for rest in dp(n - k, m - 1):
            yield (k,) + rest
        
print(sum(multinomial(hist) for hist in dp(18, 10)) * 9 // 10)
