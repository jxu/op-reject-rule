# Recursive solution f(n)
# Define in terms of smaller f: ex. 1110xxxx, x = f(n-4)
# The solution is also f(n) = f(n-1) + ... + f(0) + f(-1)
def f(n):
    if n < 3: return 1

    s = 1  # No blocks solution
    for i in range(1, n-1):
        s += i * f(n-i-3)  # Ways after red block
    return s

print(f(50))