(* f[k, l] is coefficient of Sum_{j=0..n} k^j *)
f[k_, l_] := Sum[(-1)^(m - k - 1) Binomial[m, k], {m, k + 1, l}]
TableForm@Table[f[k, l], {l, 1, 8}, {k, 0, l - 1}]

(*
1
0	2
1	-1	3
0	3	-3	4
1	-2	7	-6	5
0	4	-8	14	-10	6
1	-3	13	-21	25	-15	7
0	5	-15	35	-45	41	-21	8
*)