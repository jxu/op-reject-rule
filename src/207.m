f[m_] := Module[{n},
   n = Floor[(Sqrt[4 m + 1] + 1)/2];
   Floor[Log2[n]]/(n - 1)];
Plot[{f[m], 1/12345}, {m, 4.4043*10^10, 4.4044*10^10}]

NSolve[f[m] < 1/12345, m, Reals]  (* Cannot be solved *)