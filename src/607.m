(* As baihacker says, easy in Mathematica! Find points along the marsh boundaries and minimize a time function. *)

y1 = x1 + 25 Sqrt[2];
y2 = x2 + 15 Sqrt[2];
y3 = x3 + 5 Sqrt[2];
y4 = x4 - 5 Sqrt[2];
y5 = x5 - 15 Sqrt[2];
y6 = x6 - 25 Sqrt[2];
dist[p_, q_] := 
 Simplify[EuclideanDistance[p, q], 
  p \[Element] Reals && q \[Element] Reals]
speeds = {10, 9, 8, 7, 6, 5, 10};
points = {{-50, 0}, {x1, y1}, {x2, y2}, {x3, y3}, {x4, y4}, {x5, 
    y5}, {x6, y6}, {50, 0}};
time = Sum[
  dist[points[[i]], points[[i + 1]]]/speeds[[i]], {i, Length[speeds]}]

(*
1/10 Sqrt[(50 + x1)^2 + (25 Sqrt[2] + x1)^2] + 
 1/9 Sqrt[(x1 - x2)^2 + (10 Sqrt[2] + x1 - x2)^2] + 
 1/8 Sqrt[(x2 - x3)^2 + (10 Sqrt[2] + x2 - x3)^2] + 
 1/7 Sqrt[(x3 - x4)^2 + (10 Sqrt[2] + x3 - x4)^2] + 
 1/6 Sqrt[(x4 - x5)^2 + (10 Sqrt[2] + x4 - x5)^2] + 
 1/5 Sqrt[(x5 - x6)^2 + (10 Sqrt[2] + x5 - x6)^2] + 
 1/10 Sqrt[(-50 + x6)^2 + (-25 Sqrt[2] + x6)^2]
*)
 
m = NMinimize[time, {x1, x2, x3, x4, x5, x6}, WorkingPrecision -> 20]
(* {13.126510858558497930, {x1 -> -31.278266607206611672, 
  x2 -> -16.009137494746593508, x3 -> -2.5023629766087517511, 
  x4 -> 9.7218829080518837896, x5 -> 20.928217636554312392, 
  x6 -> 31.278266607206611672}} *)
  
N[First@m, 12]
(* 13.1265108586 *)
  

 