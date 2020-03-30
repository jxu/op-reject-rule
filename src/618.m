$RecursionLimit = Infinity;
S[k_, i_ /; i < 1] := 0;
S[k_ /; k <= 0, i_] := Boole[k == 0];
S[k_, i_] := S[k, i] = Mod[S[k, i - 1] + Prime[i] S[k - Prime[i], i], 10^9];
S[Fibonacci[24], PrimePi[Fibonacci[24]]]