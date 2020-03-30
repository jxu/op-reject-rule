(* Testing Mathematica's memoization capabilities.
   Mathematica on Linux and Windows can't compute recursion directly 
   (i.e. S[kmax, imax]) so we need to compute in steps
   https://mathematica.stackexchange.com/a/203584 

   The computation still runs out of memory but in theory it works...
*)

$RecursionLimit = Infinity;
kmax = Fibonacci[24]; imax = PrimePi[kmax];
S[k_, i_ /; i < 1] := 0;
S[k_ /; k <= 0, i_] := Boole[k == 0];
S[k_, i_] := S[k, i] = Mod[S[k, i - 1] + Prime[i] S[k - Prime[i], i], 10^9];

(* Progress bar for fun. Credit: Brett Champion *)
MemoryConstrained[
 Monitor[
  Do[S[k, i], {i, imax}, {k, kmax}],
  Row[{ProgressIndicator[i, {1, imax}], StringForm["``/``", i, imax]}, " "]
  ],
 8*10^9
 ]

Mod[Sum[S[Fibonacci[k], kmax], {k, 2, 24}], 10^9]
