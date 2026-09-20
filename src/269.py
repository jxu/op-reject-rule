from functools import cache

# Y is multi-state for multiple x
@cache
def f(Y, l):
    #print(Y, l)
    if l == 0:
        return any(y == 0 for y in Y)

    s = 0

    for a in range(10):
        newY = list(Y)
        for i in range(10):
            x = i - 9
            y = Y[i]
            if y is None: 
                continue  # leave as is?

            if x == 0:
                # save Y[i] as current a
                newY[i] = a
                pass
            elif (y - a) % x == 0:
                newY[i] = (y - a) // x
            else:
                newY[i] = None

        newY = tuple(newY)
        #print("a", a, newY)
        s += f(newY, l-1)

    return s 


print(f((0,)*10, 16))
