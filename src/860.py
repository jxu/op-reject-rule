# Gary moves (and vice versa for Sally):
# 1. remove 1 coin from GG; 2. remove 2 coins from GG
# 3. remove 2 coins from GS; 4. remove 1 coin from G
# It's always better for Gary to remove 1 coin from GG rather than both,
# since it gives him an extra move. So Gary's moves remove 1 gold coin.
# The priority is:
# 1. remove GS, since it decreases silver
# 2. remove SG, since if not next turn Sally could decrease gold
# 3. remove one gold from G or GG

# From the given examples, GG SS and SG GS are fair combos.
# But this gives (2n choose n)^2 (A002894), 63504 = F(10) - 90
# After thinking for a while, I found the fair example GS GS GS GS SS
# Gary start  -> GS GS GS SS   -> G GS GS SS -> G GS SS   -> G G SS -> fair
# Sally start -> G GS GS GS SS -> G GS GS SS -> G G GS SS -> G G SS -> fair
# (the fair "unit" is actually 5 coins: GS GS S)
# because n is even, the fair combo is double: 8xGS 2xSS.

# Then I assumed these were the only fair combos. I think the two combos
# cover all optimal move and response actions.
# 8xGS 2xSS and 8xSG 2xGG are actually pairs of GG SS and SG GS, so
# "cancel out". Therefore the cases are:
# 1. j SS, j GG, k GS, k SG
# 2. j+2i SS, j GG, k+8i GS, k SG
# 3. j SS, j+2i GG, k GS, k+8i SG
# These can be combined into one case, count twice if i>0.


from number import mod_inv
m = 989898989

def fact_mod_list(n, m):
    """Compute [0!, ..., n!] mod m in O(n)."""
    fact_mod = [1] * (n + 1)
    for i in range(2, n+1):
        fact_mod[i] = (i * fact_mod[i-1]) % m
    return fact_mod

def inv_list(l, m):
    return [mod_inv(x,m) for x in l]


def F(n):
    n //= 2  # makes math a little nicer
    fact_mod = fact_mod_list(2*n, m)
    fact_inv = inv_list(fact_mod, m)

    s = 0
    for i in range (0, n//5+1):
        for j in range((n-5*i) + 1):
            k = (n - 5*i - j)
            assert 2*j + 2*k + 10*i == 2*n

            r = (1 + (i > 0))  # double if SG is more or GS is more
            for t in (fact_mod[2*n], fact_inv[j], fact_inv[j+2*i],
                      fact_inv[k], fact_inv[k+8*i]):
                r = (r * t) % m
            s = (s + r) % m

    return s


print(F(9898))