(* Explicit formula from generating function:
     P(M) is defined as Sum_{k=1..Inf} F_{kM-1} x^k where x = 2^-M
   Derived from recurrence F_{kn} = L_k F_{k(n-1)} - (-1)^k F_{k(n-2)}
 *)

p[m_] := Module[
  {x}, x = 2^-m;
  f[k_] := Fibonacci[k m - 1];
  Return[(f[1] x + (f[2] - LucasL[m] f[1]) x^2)/(1 - x LucasL[m] + (-1)^m x^2)]
  ]

p[2]
p[3]