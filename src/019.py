first_sundays = 0
day = (1 + 365) % 7 # Jan 1 1900 Monday + 1 year

for y in range(1901, 2001):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if y % 4 == 0: # 2000 is leap year
        months[1] = 29
        
    for month in months:
        if day == 0: first_sundays += 1
        day = (day + month) % 7
        
print(first_sundays)
        

        

        