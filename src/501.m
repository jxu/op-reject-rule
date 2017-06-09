(* 51 seconds on desktop, since Mathematica's PrimePi is very fast *)
n = 10^12;
primes = Prime@Range@PrimePi@Sqrt[n];
primesCbrt = Prime@Range@PrimePi@CubeRoot[n];
count = PrimePi[n^(1/7)] +
   Total[Function[p, PrimePi[n/p^3] - Boole[(n/p^3) >= p]] /@ 
     primesCbrt];
(* Todo: rewrite in nice functional way *)
For[pi = 1, pi <= Length[primesCbrt], pi++,
  p = primesCbrt[[pi]];
  For[qi = pi + 1, primes[[qi]] <= Sqrt[n/p], qi++,
   count += PrimePi[n/(p*primes[[qi]])] - qi;
   ];
  ];
Print[count];


(* Cleaner version that won't run in time *)
n = 10^6;
primesCbrtN = Prime@Range@PrimePi@CubeRoot[n];
PrimePi[n^(1/7)] +
 Sum[PrimePi[n/p^3], {p, primesCbrtN}] - PrimePi[n^(1/4)] +
 Sum[PrimePi[n/(p q)] - PrimePi[q], {p, primesCbrtN}, {q, 
   Prime[Range[PrimePi[p] + 1, PrimePi[Sqrt[n/p]]]]}]