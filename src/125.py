all_nums = set()
for i in range(1, 10001):
    p_sum = i**2
    for j in range(i+1, 10001):
        p_sum += j**2
        if p_sum >= 10**8: break
        if str(p_sum) == str(p_sum)[::-1]:
            print(i, j, p_sum)
            if p_sum in all_nums: print("dupe") 
            all_nums.add(p_sum)

print(sum(all_nums))