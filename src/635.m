a2[p_] := (1/p) (Binomial[2 p, p] + 2 (p - 1));
a3[p_] := (1/p) (Binomial[3 p, p] + 3 (p - 1));
Table[a3[p], {p, Prime@Range[10]}]

a[q_, p_] :=
 Length@Select[Subsets[Range[q p], {p}], Divisible[Total[#], p] &]
(* a[2,2] == 2, a[3,2] == 6 *)