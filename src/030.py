# Upper limit for range: 5*9^5 < 99999, 6*9^5 > 999999
s = 0
for i in range(2, 10**6):
        p = sum(int(d)**5 for d in str(i))
        if p == i: s += i
        
print(s)
        
# One-line horror
print(sum(i for i in range(2, 10**6) if sum(int(d)**5 for d in str(i))==i))