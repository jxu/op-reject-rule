(* A string with one spot with characters in ascending order is the same as 
  two strings of descending order separated by one ascension.
  Write the first descending string as xxx...x and the second as yyy...y
  There are 2^n strings made up of x and y. Exclude 2 that are only x and only
  y, and there are n-1 forbidden strings that have no ascension:
  xy...y, xxy...y, xxxy...y, ..., xxx...xy.
  So the closed form solution is (26 choose n) * (2^n - 2 - (n-1))  *)

Max[Table[Binomial[26, n]*(2^n - n - 1), {n, 1, 26}]]