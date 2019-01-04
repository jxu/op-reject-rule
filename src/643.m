(* Rewrite in terms of Mobius function *)
f[n_] := Sum[Binomial[Floor[n/(2 k)], 2]*MoebiusMu[k], {k, 1, n, 2}]
f[100] == 1031

(* Mertens function and sum of odd mobius terms *)
m[n_] := Sum[MoebiusMu[k], {k, 1, n}];
mo[n_] := Sum[MoebiusMu[k], {k, 1, n, 2}];

(* Since for odd n, mu(2n) = -mu(n) and mu(4n) = mu(8n) = ... = 0,
   we have identity m(n) = mo(n) - mo(n/2)  *)
Table[m[n], {n, 1, 20}] == Table[mo[n] - mo[n/2], {n, 1, 20}]