(* 18 seconds with Sum on desktop, since Mathematica's PrimePi is very fast *)
n = 10^12;
cbrtNindex = PrimePi[CubeRoot[n]];
PrimePi[n^(1/7)] +
 Sum[PrimePi[n/Prime[i]^3], {i, 1, cbrtNindex}] - PrimePi[n^(1/4)] +
 Sum[PrimePi[n/(Prime[i]*Prime[j])] - j,
  {i, 1, cbrtNindex},
  {j, i + 1, PrimePi[Sqrt[n/Prime[i]]]}]