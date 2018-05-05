shuffle[d_] := Riffle @@ Partition[d, Length[d]/2];
NestList[shuffle, Range[0, 9], 6]

2*Position[Table[MultiplicativeOrder[2, 2 n + 1], {n, 0, 1000}], 8]