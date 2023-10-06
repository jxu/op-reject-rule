# linear recurrence with GF
# x^6/((1-x)(1-x^2)(1-x^3)(1-x^4)(1-x^6)) = sum a_n x^n
# Denominator = -x^16 +x^15 +x^14 -2x^11 +x^10 -x^9 +x^7 -x^6 +2x^5 -x^2 -x +1
# Multiplying by denominator and equating coefficients, we get a recurrence
n = 55106
c = [0]*(n+1)
c[:16] = [0, 0, 0, 0, 0, 0, 1, 1, 2, 3, 5, 6, 10, 12, 17, 21]
for i in range(16, n+1):
    c[i] = (c[i-1] + c[i-2] - 2*c[i-5] + c[i-6] - c[i-7] + c[i-9]
            - c[i-10] + 2*c[i-11] - c[i-14] - c[i-15] + c[i-16])

print(c[-1])

