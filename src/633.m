(* The idea is to use the sum of the product of all 7-tuples of
   $1/p^2$ for prime $p$.
   This can be written in terms of $(s), the prime zeta function:
   P(s) = \sum_p p^(-s)

   The polynomials used for inclusion-exclusion correspond to the cyclic index
   of the symmetric group with order 7, up to sign. http://oeis.org/A181897
   Not sure why. Then calculate the same for 8 and 9.
   https://math.stackexchange.com/q/2890574    *)

primeZeta[n_] := primeZeta[n] = Total[N[Prime@Range[10^5]^-n]];
f[m_, zeta_] := ((-1)^m)
  CycleIndexPolynomial[SymmetricGroup[m], -zeta /@ Range[2, 2 m, 2]];
Total@Table[-(-1)^k Binomial[k, 7]*f[k, primeZeta], {k, 7, 9}]
