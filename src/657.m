(* Original formula using non-empty strings (add 1 at end) *)
Unprotect[Power]; Power[0, 0] = 1; Protect[Power];
i[l_, n_] := Sum[(-1)^(l - k + 1) Binomial[l, k] Sum[k^j, {j, 0, n}], {k, 0, l - 1}]

i[l_, n_] :=
  1 - (-1)^(l - 1) l n -
  Sum[(-1)^k Binomial[l, l - k] (((l - k)^(n + 1) - 1)/(l - k - 1) - 1), {k, 1, l - 2}]

(* Slightly cleaner formula *)
i[l_, n_] := Sum[(-1)^(l - k + 1) Binomial[l, k] Sum[k^j, {j, 0, n}], {k, 0, l - 1}];

i[3, 4]
