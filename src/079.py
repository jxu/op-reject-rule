# BFS
with open("p079_keylog.txt") as f:
    logins = f.read().split('\n')[:-1]
    
logins = set(logins)
   
passcodes = [(l, {l}) for l in logins]

while True:
    new_passcodes = []
    for p in passcodes:
        print(p)
    
    
    break