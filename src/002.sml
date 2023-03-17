(* ideally should be memoized *)
fun fib 1 = 1
  | fib 2 = 2
  | fib n = fib (n-1) + fib (n-2)

fun f n = 
  if fib n > 4000000 then 0
  else (if fib n mod 2 = 0 then fib n else 0) + (f (n+1))
;
f 1 
