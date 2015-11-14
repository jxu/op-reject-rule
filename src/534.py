n = 8
count = 0

def f(board, l):
    if l == n:
        #print(board)
        global count
        count += 1
        return

    for x in range(n):
        valid = True
        for j in range(l):
            if x == board[j] or l-j == abs(x - board[j]):
                valid = False
                break

        if valid: f(board + [x], l+1)



for start in range(n):
    f([start], 1)
print(count)


