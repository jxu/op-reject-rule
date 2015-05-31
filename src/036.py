# Remove leading '0b' in binary string
print(sum(i for i in range(10**6) if str(i) == str(i)[::-1] and str(bin(i))[2:] == str(bin(i))[2:][::-1]))

