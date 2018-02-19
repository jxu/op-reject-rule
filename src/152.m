(* Note that in the given solutions, the numbers that are multiples of 7 are 
   7, 28, 35. Indeed 1/p^2 + 1/(4p)^2 + 1/(5p)^2 = 441/400p^2, and 7^2 | 441.
   In fact, 7 is the largest prime factor of the numbers in the example.
*)

Map[Function[x,{x,Total[(p*x)^-2]}],
  Subsets[Range[1,6],{2,6}]]

pairs = {#, Total[#^-2]} & /@ Subsets[Range[1, 11], {2, 11}];
Select[pairs, 13^2\[Divides]Numerator[Last@#] && 13 Max[First@#] <= 80 &]

(* The largest prime factor of a denominator must be 2, 3, 5, 7, or 13 only *)
Table[p*First /@
   Select[pairs, (p^2\[Divides]Numerator@Last@#) && p*Max@First@# <= 80 &],
 {p, Table[Prime[n], {n, 4, 10}]}]

Select[Range[2, 80], Max[First /@ FactorInteger@#] <= 7 &]