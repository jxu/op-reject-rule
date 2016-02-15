# Methods credit to Rosetta Code (R has a built-in function!?)
numeral_values = (('I',1), ('IV',4), ('V',5), ('IX',9), ('X',10), ('XL',40), ('L',50), ('XC',90),
                  ('C',100), ('CD',400), ('D',500), ('CM',900), ('M',1000))

def roman_decode(roman):
    total = 0
    for symbol, value in reversed(numeral_values):
        while roman.startswith(symbol):
            total += value
            roman = roman[len(symbol):]
    return total


def roman_encode(x):
    ret = []
    for value in reversed(numeral_values):
        n, x = divmod(x, value[1])
        ret.append(value[0]*n)
    return ''.join(ret)


saved = 0
for raw_line in open("p089_roman.txt"):
    line = raw_line.strip()
    minimal = roman_encode(roman_decode(line))
    print(line, minimal, len(line)-len(minimal))
    saved += len(line)-len(minimal)

print(saved)