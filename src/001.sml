fun f 0 = 0 
  | f n = (if ((n mod 3 = 0) orelse (n mod 5 = 0)) 
           then n else 0) + f (n-1);
f(999);
