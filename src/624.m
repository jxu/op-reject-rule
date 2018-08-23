(* M=2: HH          Pr(M=2) = 1/4
   M=3: THH         Pr(M=3) = 1/8
   M=4: XTHH        Pr(M=4) = 2/16
   M=5: XXTHH       Pr(M=5) = 3/32
   M=6: XXXTHH      Pr(M=6) = 5/64
                    Pr(M)   = F_{M-1} / 2^M

   XXX...X is a string of tosses without two heads in a row.
   There are F_{M-1} possible strings.
   Every nth probability has n|M.

   Explicit formula from generating function:
     P(n) is defined as Sum_{k=1..Inf} (F_{kn-1} x^k) where x = 2^-n
   Derived from recurrence F_{kn} = L_k F_{k(n-1)} - (-1)^k F_{k(n-2)}
 *)

p[n_] := Module[
  {x}, x = 2^-n;
  f[k_] := Fibonacci[k n - 1];
  (f[1] x + (f[2] - LucasL[n] f[1]) x^2)/(1 - x LucasL[n] + (-1)^n x^2)
  ];

(* p[2] = 3/5, p[3] = 9/31 *)

(* Calculate Fibonacci mod using the Fibonacci matrix form and binary mod exp *)
fibMod[n_, mod_] :=
  Module[{base, result, exp},
   exp = n;
   base = {{1, 1}, {1, 0}};
   result = IdentityMatrix[2];
   While[exp > 0,
    result = If[Mod[exp, 2] == 1, Mod[result.base, mod], result];
    exp = BitShiftRight[exp];
    base = Mod[base.base, mod];
    ];
   result[[1, 2]]
   ];

(*L_n = F_{n+1} + F_{n-1} *)
lucasMod[n_, mod_] :=
  Mod[fibMod[n - 1, mod] + fibMod[n + 1, mod], mod];


mod = 1000000009; n = 10^18;
(* Use formula from p[n] but multiply numerator and denominator by x^-2 = 2^2n
   to get integer numerator a and denominator b  *)
a = Mod[fibMod[n - 1, mod]*PowerMod[2, n, mod] +
    fibMod[2 n - 1, mod] - lucasMod[n, mod]*fibMod[n - 1, mod], mod];
b = Mod[PowerMod[2, 2 n, mod] -
    PowerMod[2, n, mod]*lucasMod[n, mod] + (-1)^n, mod];

Mod[a*ModularInverse[b, mod], mod]