# I had the pleasure of meeting Jay Kadane himself and asking him about his
# algorithm. He told me that in the 80s he had a colleague who was working on a
# problem and came up with an O(n log n) time algorithm but couldn't prove it
# was optimal. Kadane said "well, I wouldn't do it that way, I'd actually do
# it this way" and that's how he came up with his namesake linear time
# algorithm. He said it was more about being at the right place at the right
# time to have an algorithm, but "I suppose it's the dream of every computer
# scientist to have an algorithm named after him".

# Maximum subarray problem 4 times, with Kadane's algorithm

def kadane(t, x, y, dx, dy):
    max_sum = max_prefix = t[y][x]
    x += dx
    y += dy
    while 0 <= x < 2000 and 0 <= y < 2000:
        max_prefix = max(t[y][x], max_prefix + t[y][x])
        max_sum = max(max_prefix, max_sum)
        x += dx
        y += dy

    return max_sum


s = [0]*4000001
for k in range(1, 4000001):
    if k <= 55:
        s[k] = (100003 - 200003*k + 300007*k**3) % 1000000 - 500000
    else:
        s[k] = (s[k-24] + s[k-55] + 1000000) % 1000000 - 500000


t = [s[2000*i+1:2000*i+2001] for i in range(2000)]

max_sum = 0
for x in range(2000):
    max_sum = max(max_sum,
                  kadane(t, x, 0, 0, 1),     # Vertical
                  kadane(t, x, 0, 1, 1),     # Diagonal upper
                  kadane(t, x, 0, -1, 1))    # Anti-diagonal upper

for y in range(2000):
    # Skip y = 0 for last 2 to save a tiny amount of time
    max_sum = max(max_sum,
                  kadane(t, 0, y, 1, 0),     # Horizontal
                  kadane(t, 0, y, 1, 1),     # Diagonal lower
                  kadane(t, 1999, y, -1, 1)) # Anti-diagonal lower

print(max_sum)
