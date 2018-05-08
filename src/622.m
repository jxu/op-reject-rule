(* ::Package:: *)

(* Testing riffle shuffle *)
shuffle[d_] := Riffle @@ Partition[d, Length[d]/2]; 
NestList[shuffle, Range[0, 9], 6]

(* A002326 *)
2*Position[Table[MultiplicativeOrder[2, 2 n + 1], {n, 0, 1000}], 8]

(* 2^60 = 1 (mod 2n+1), so consider factors of 2^60 - 1 *)
First@Total@Select[Table[{n+1,MultiplicativeOrder[2,n]},{n,Divisors[2^60-1]}],Last[#]==60&]
Total[1+Select[Divisors[2^60 - 1], MultiplicativeOrder[2, #] == 60 &]  (* Shorter solution by Zach-Lurf *)



