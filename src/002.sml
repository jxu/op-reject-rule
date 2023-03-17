(* ideally should be memoized *)
fun fib 1 = 1
  | fib 2 = 2
  | fib n = fib (n-1) + fib (n-2)

fun f n = 
  if fib n > 4000000 then []
  else (fib n) :: (f (n+1))

val sum = foldl op+ 0
;
sum (List.filter (fn x => x mod 2 = 0) (f 1))
    
