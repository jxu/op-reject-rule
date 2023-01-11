
from number import combination

N = 3
M = 2  #  answer digits

def dfs(target_digit,
        cur_sum=0,
        depth=0,  # digits in current x
        used_digit=False,
        x=0):
    if depth == M:
        if cur_sum <= target_digit and used_digit:
            print(x)
            return [x]
        else: return []

    s = []
    # append other digit
    for d in range(10):
        if d + cur_sum <= target_digit:
            s.extend(dfs(target_digit,
                     d + cur_sum,
                     depth + 1,
                     used_digit,
                     10 * x + d))

    # append target digit
    if not used_digit:
        used_digit = True
        s.extend(dfs(target_digit,
                 cur_sum,
                 depth + 1,
                 True,
                 10 * x + target_digit))

    return s

s = 0
for target in range(10):
    for dsn in set(dfs(target)):
        s += dsn

print(s)