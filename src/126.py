# My hardest challenge yet (?)
# ========================
#             X+
#      X+    X  X
# X+  X  X  X    X
#      X+    X  X
#             X+
# Start with 1x1x1 cube. For n layers, it takes: 2, 6, 18, 38, ... (4n^2 + 2; A005899)
# Each increase in h, l, w adds a [maximal] "middle" ring
# Define H, L, W as increases in each dimension from a 1x1x1 cube (H = h-1, L = l-1, W = w-1)
# The middle ring size for an increase in L is L(2H + 2W + 4n)  *Diagram above
# Subtract the overlap of the rings: 2HW
# Similar process for H, W, to get:
# c(n, H, L, W) = (4n^2 + 2) + L(2H + 2W + 4n) - 2HW + W(2H + 2L + 4n) - 2HL + H(2L + 2W + 4n) - 2LW
# = (4n^2 + 2) + 4n(H + L + W) + 2HL + 2HW + 2LW

def c(n, H, L, W):
    return 4*n**2 + 2 + 4*n*(H + L + W) + 2*H*L + 2*H*W + 2*L*W

MAX_CUBES = 20000  # tuning
MAX_INT = MAX_CUBES
C = [0] * MAX_CUBES

for H in range(0, MAX_INT):
    if c(1, H, H, H) >= MAX_CUBES: break

    for L in range(H, MAX_INT):
        if c(1, H, L, H) >= MAX_CUBES: break

        for W in range(L, MAX_INT):
            if c(1, H, L, W) >= MAX_CUBES: break

            for n in range(1, MAX_INT):
                if c(n, H, L, W) >= MAX_CUBES: break

                C[c(n, H, L, W)] += 1

for x in C:
    if x == 1000:
        print(C.index(x))
        break