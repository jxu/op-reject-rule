# My hardest challenge yet
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
