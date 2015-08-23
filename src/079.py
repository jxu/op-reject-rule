# Topological Sort
with open("p079_keylog.txt") as f:
    logins = f.read().split('\n')[:-1]
    
logins = set(logins)


adj_list = set()
digits = set()
for l in logins:
    adj_list.add((l[0], l[1]))
    adj_list.add((l[1], l[2]))
    for c in l:
        digits.add(c)

s = ""
    
while adj_list:
    rem = digits.copy()
    for a in adj_list:
        try: 
            rem.remove(a[1])
        except:
            pass
        
    digits.remove(list(rem)[0])
    s += list(rem)[0]
    
    new_adj_list = set()
    
    for a in adj_list:
        if a[0] != list(rem)[0]:
            new_adj_list.add(a)
            
            
    adj_list = new_adj_list
            
print(s + '0')
