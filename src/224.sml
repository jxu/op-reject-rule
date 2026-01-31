val M = 75000000
fun f (a, b, c) = 
  if a + b + c > M then 0
  else 1 +
    f   ( a - 2*b + 2*c,  2*a - b + 2*c,  2*a - 2*b + 3*c) +
    f   ( a + 2*b + 2*c,  2*a + b + 2*c,  2*a + 2*b + 3*c) +
    (if a = b then 0 else 
      f (~a + 2*b + 2*c, ~2*a + b + 2*c, ~2*a + 2*b + 3*c))
;
f (2, 2, 3)

