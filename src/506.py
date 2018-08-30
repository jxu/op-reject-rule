# After 15 values, v_i repeats but with a prefix that is a rotation of 123432
# Ex. v_16 is 123432 1, v_17 is 234321 2, etc. (see 506.csv)
# The prefix only depends on i mod 15.
# To encode the repeated prefixes, use prefix * (10^0 + 10^6 + ...)
# Then shift over by how many digits seq is and add seq.
# Ex. 123432 * (10^0 + 10^6) * 10^1 + 1 = 123432 123432 1
# Calculate sum of all values for each congruence class mod 15

prefix = (123432, 234321, 343212, 432123, 321234, 212343)
seq = (0, 1, 2, 3, 4, 32, 123, 43, 2123, 432, 1234, 32123, 43212, 34321, 23432)
seq_len = (0, 1, 1, 1, 1, 2, 3, 2, 4, 3, 4, 5, 5, 5, 5)
pos     = (0, 0, 1, 2, 3, 4, 0, 3, 5, 3, 0, 4, 3, 2, 1)

M = 123454321

def sum_pow10(t):
    # Calculates Sum_[k=0..t] (t-k) 10^(6k) mod M
    # = 10^0 + (10^0 + 10^6) + ... + (10^0 + 10^6 + ... + 10^(6(t-1)))
    # 1, 1 000002, 1 000002 000003, etc.
    # Mathematica: (-1000000 + 10^(6 + 6t) - 999999t) / 999998000001
    return (96017284 * (-1000000 + pow(10, 6+6*t, M) - 999999*t)) % M

def S(n):
    s = 0
    for i in range(15):
        # For congruence class i, t counts how many times prefix occurs in
        # highest v_n in congruence class
        t = n//15 - (i%15 > n%15)
        s = (s + prefix[pos[i]]*sum_pow10(t) * 10**seq_len[i] + (t+1)*seq[i])%M

    return s

print(S(10**14))