# Exponential generating function idea
# 18th coef of (x^0/0! + x^1/1! + x^2/2! + x^3/3!)^10
using Polynomials
p = Polynomial([1, 1, 1//2, 1//6])
println(Int((9 // 10) * factorial(18) * (p^10)[18]))