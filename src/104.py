# 10 digit margin for first digits
hi_a = hi_b = 1
lo_a = lo_b = 1
for i in range(1000000):
	hi_c = hi_a + hi_b
	if hi_c >= 10**19:
		hi_a, hi_b, hi_c = hi_a//10, hi_b//10, hi_c//10

	lo_c = (lo_a + lo_b)%10**9

	if set(str(lo_c)) == set(str(hi_c)[:9]) == set("123456789"):
		print(str(hi_c) + "..." + str(lo_c), i+3)

	hi_a, hi_b = hi_b, hi_c
	lo_a, lo_b = lo_b, lo_c
