# Generatingfunctionology
# =======================

# Likely the hardest problem I've ever done

# Key observation:
# Equiangular hexagons are fully determined by their sides
# (a,b,c,d,e,f), with constraints
#
#   a + b = d + e
#   b + c = e + f
#   c + d = f + a
#
# (The last equation is redundant.)
#
# The invariant is
#
#   t = a - d = e - b = c - f
#
# giving the parameterization
#
#   a = d + t
#   e = b + t
#   c = f + t

# With Burnside's Lemma
# ---------------------

# Hexagons without considering congruence (identity action)

# Case t > 0: a = d + t, e = b + t, c = f + t
# Therefore
#
#   a + b + c + d + e + f = 2b + 2d + 2f + 3t <= N
#
# After shifting positive variables:
#
#   2b' + 2d' + 2f' + 3t' + s = N - 9
#
# GF: x^9 / ((1-x^2)^3 (1-x^3) (1-x))
#
# Case t < 0 is symmetric.
# Case t = 0: a = d, b = e, c = f
#
#   2a + 2b + 2c <= N
#
# After shifting:
#
#   2a' + 2b' + 2c' + s = N - 6
#
# GF: x^6 / ((1-x^2)^3 (1-x))
#
# Final GF: (x^6 + x^9) / ((1-x^2)^3 (1-x^3) (1-x))

N = 55106

R.<x> = PowerSeriesRing(QQ, default_prec=N+1)

identity_gf = (x^6 + x^9) / ((1-x^2)^3 * (1-x^3) * (1-x))

ri = identity_gf[N]
print("ri =", ri)

# ±60 degree rotation

#   a = b = c = d = e = f
#
# Count: floor(N/6)

r60 = N // 6
print("r60 =", r60)

# ±120 degree rotation

#   a = c = e
#   b = d = f
#
# Count positive integer solutions to
#
#   3a + 3b <= N
#
# Equivalently:
#
#   a + b + s = floor(N/3) + 1
#
# with stars-and-bars:
#
#   binomial(floor(N/3), 2)

r120 = binomial(N // 3, 2)
print("r120 =", r120)

# 180 degree rotation

#   a = d
#   b = e
#   c = f
#
# Count:
#
#   2a + 2b + 2c <= N
#
# Equivalently:
#
#   a + b + c + s = floor(N/2) + 1
#
# giving:
#
#   binomial(floor(N/2), 3)

r180 = binomial(N // 2, 3)
print("r180 =", r180)

# Reflection through vertex

#   a = b = d = e
#   c = f
#
# Positive solutions:
#
#   4a + 2b <= N
#
# After shifting:
#
#   4a' + 2b' + s = N - 6
#
# GF: x^6 / ((1-x^4)(1-x^2)(1-x))

vertex_gf = x^6 / ((1-x^4) * (1-x^2) * (1-x))

sv = vertex_gf[N]
print("sv =", sv)

# Reflection through side

#   c = e
#   b = f
#   a + b = d + e
#
# Case t > 0:
#
#   a = d + t
#   e = c = b + t
#
# Positive solutions:
#
#   2d + 4b + 3t <= N
#
# After shifting:
#
#   2d' + 4b' + 3t' + s = N - 9
#
# GF: x^9 / ((1-x)(1-x^2)(1-x^3)(1-x^4))
#
# Case t = 0 has the same GF as the
# reflection-through-vertex case.
#
# Final GF:
#
#   (x^6 + x^9) / ((1-x)(1-x^2)(1-x^3)(1-x^4))


side_gf = (x^6 + x^9) / ((1-x) * (1-x^2) * (1-x^3) * (1-x^4))

ss = side_gf[N]
print("ss =", ss)

# The magic formula
# (I honestly cannot believe this actually worked)

burnside = (ri + 2*r60 + 2*r120 + r180 + 3*ss + 3*sv) / 12
print("Burnside count =", burnside)

# Direct Congruence Calculation
# -----------------------------

# It turns out letting
#
#   b <= d <= f,  t >= 0
#
# parameterizes the hexagons up to congruence exactly.
#
# For t < 0, swap (a,d), (b,e), (c,f) as a 180-degree rotation.
#
# Put
#
#   d = b + y
#   f = d + z = b + y + z
#
# Then
#
#   a + b + c + d + e + f = 6b + 4y + 2z + 3t <= N
#
# Equivalently:
#
#   6b' + 4y + 2z + 3t + s = N - 6
#
# All-in-one GF:
#
#   x^6 / ((1-x)(1-x^2)(1-x^3)(1-x^4)(1-x^6))


direct_gf = x^6/ ((1-x) * (1-x^2) * (1-x^3) * (1-x^4) * (1-x^6))

sN = direct_gf[N]
print("Direct congruence count =", sN)
