(* Maybe use Memoize from https://github.com/msullivan/sml-util *)
open Int64

fun a 1 = 1
  | a n = if n mod 2 = 0 
          then 2 * a (n div 2)
          else a (n div 2) - 3 * a (n div 2 + 1)

fun S N = if N mod 2 = 1 
          then 4 - 3 * a (N div 2 + 1)
          else S (N + 1) - a (N + 1)
;
S 1000000000000
