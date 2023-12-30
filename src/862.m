(* The combinatorics solution is using exponential generating functions
(credit: vikt)
For a string with c0 0s, c1 1s, etc. the number of permutations for each
equivalence class O is |O| = k! / (c0!c1!...c9!)
and our answer is sum over all classes O of (|O|^2 - |O|)/2

The EGF where [x^k/k!] counts the sum of all |O| is
(x^0/0! + x^1/1! + ...)^10 = e^(10x)
Where each series term represents picking ci of digit i.

To count sum of all |O|^2, just square the coefficients:
(x^0/0!^2 + x^1/1!^2 + ...)^10

To handle excluding leading zeros, observe c0/k of the permutations have a
leading zero. Therefore the first series, representing c0, is modified as
(1-0/k) x^0/0! + (1-1/k)x^1/1! + ... = (1-x/k) e^x
Similar for the squared terms. The final result is (w2-w1)/2, where
w1 = [x^k/k!](1-x/k)e^(10x) = 9 * 10^(k-1)
w2 = [x^k/k!^2] (sum_i=0..inf (1-i/k)^2 x^i/i!^2) (sum_i=0..inf x^i/i!^2)^9
*)
k = 12

g1 = ExponentialGeneratingFunction[1 - i/k, i, x] *
  ExponentialGeneratingFunction[1, n, x]^9

(*  GeneratingFunction[((1 - i/k)/i!)^2, i, x] doesn't work *)
g2 = Sum[x^i ((1 - i/k)/i!)^2, {i, 0, \[Infinity]}] *
 GeneratingFunction[(1/n!)^2, n, x]^9

SeriesCoefficient[((k!)^2 g2 - k! g1)/2, {x, 0, k}]