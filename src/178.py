# [0-9] - [0-8] - [1-9] + [1-8]
d09 = [0] + [1]*9  # Don't start with 0
d08 = [0] + [1]*8
d19 = [1]*9
d18 = [1]*8

def step(digits):
    new_digits = [0] * len(digits)
    for i in range(len(digits)):
        if i > 0: new_digits[i] += digits[i-1]
        if i < len(digits)-1: new_digits[i] += digits[i+1]

    return new_digits


result = 0
for num_length in range(40):
    result += sum(d09) - sum(d08) - sum(d19) + sum(d18)
    d09 = step(d09)
    d08 = step(d08)
    d19 = step(d19)
    d18 = step(d18)

print(result)

