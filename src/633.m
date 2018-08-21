altTotal[x_] := Total@x[[;; ;; 2]] - Total@x[[2 ;; ;; 2]];

(*Memoize prime Zeta function *)
primeZeta[s_] := primeZeta[s] = Total@N[(Prime@Range[10^6])^-s];

inex[n_, zeta_: primeZeta] :=
 Module[{productPairs, summands},
  productPairs = Subsets[Range[n], {2}];
  summands = Table[
    conComp = 
     ConnectedComponents /@ 
      Map[Join[#, Table[{i, i}, {i, 1, n}]] &, 
       Subsets[productPairs, {depth}]];
    Total[Times @@@ Map[zeta[2 Length[#]] &, conComp, {2}]],
    {depth, 1, Length[productPairs]}];
  Return[(zeta[2]^n - altTotal[summands])/n!]
  ]
