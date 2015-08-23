# Topological Sort
with open("p079_keylog.txt") as f:
    logins = f.read().split('\n')[:-1]
    
logins = set(logins)

adj_list = set()
digits = set()
for l in logins:
    adj_list.add((l[0], l[1]))
    adj_list.add((l[1], l[2]))
    for c in l: digits.add(c)

s = ""
while adj_list:
    rem = digits.copy()
    for a in adj_list:
        if a[1] in rem: 
            rem.remove(a[1])
    
    rem = list(rem)[0]      
    digits.remove(rem)
    s += rem

    adj_list = set(a for a in adj_list if a[0] != rem)
    
print(s + list(digits)[0])
