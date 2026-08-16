using Primes, Memoize, Printf

ps = primes(10^6)

@memoize p(k) = sum((Float64(q)^2 - 1)^-k for q in ps)

@memoize e(k) = 
    k == 0 ? 1 :
    sum((-1)^(j-1) * e(k-j) * p(j) for j in 1:k) / k

c(k) = (6 / pi^2) * e(k)

@printf("%.4e\n", c(7))