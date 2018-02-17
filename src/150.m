(* Note that in the given solutions, the numbers that are multiples of 7 are 
   7, 28, 35. Indeed 1/p^2 + 1/(4p)^2 + 1/(5p)^2 = 441/400p^2, and 441=3*3*7*7
   In fact, 7 is the largest prime factor of the numbers in the example.
*)

Map[Function[x,{x,Total[(p*x)^-2]}],
  Subsets[Range[1,6],{2,6}]]

numPairs=Map[Function[x,{x,Numerator[Total[(p*x)^-2]]}],
  Subsets[Range[1,10],{2,10}]];
Select[numPairs,Divisible[#[[2]],7]&]