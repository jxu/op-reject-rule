from functools import cache

@cache
def f(Y, l):
    if l == 0:
        return int(any(y == 0 for y in Y))

    s = 0
    for a in range(10):
        newY = list(Y)
        for i in range(10):
            x = i - 9
            y = Y[i]
            if y is None: 
                continue  # leave as is

            if x == 0:
                # special case for constant term
                newY[i] = a if l == 1 else 0
            elif (y - a) % x == 0:
                newY[i] = (y - a) // x
            else: 
                newY[i] = None  # special invalid value

        s += f(tuple(newY), l-1)

    return s 


print(f((0,)*10, 16))
