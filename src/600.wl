(* ::Package:: *)

(* ::Title:: *)
(*Generatingfunctionology*)


(* ::Text:: *)
(*Key observation: Equiangular hexagons are fully determined by their sides (a,b,c,d,e,f), with constraints a + b = d + e, b + c = e + f, c + d = f + a (last is redundant). *)
(*The invariant is t = a - d = e - b = c - f, giving the parameterization a = d + t, e = b + t, c = f + t.*)
(**)


(* ::Chapter:: *)
(*With Burnside's Lemma*)


(* ::Text:: *)
(*First, calculate total hexagons without congruence.  *)


(* ::Input:: *)
(*s1=Series[x^9/((1-x^2)^3(1-x^3)(1-x)),{x,0,20}]*)


(* ::Input:: *)
(*s0=Series[x^6/((1-x^2)^3(1-x)),{x,0,20}]*)


(* ::Input:: *)
(*2*s1+s0 (*total hexagons without congruence*)*)


(* ::Input:: *)
(*Expand[(1-x^2)^3(1-x^3)(1-x),x]*)


(* ::Input:: *)
(*Rest[-CoefficientList[(1-x^2)^3(1-x^3)(1-x),x]]*)


(* ::Input:: *)
(*LinearRecurrence[Rest@-CoefficientList[(1-x^2)^3(1-x^3)(1-x),x],{0,0,0,0,0,1,1,4,6,12},{1,55106}]*)


(* ::Input:: *)
(*Expand[(1-x^2)^3(1-x),x]*)


(* ::Input:: *)
(*LinearRecurrence[Rest@-CoefficientList[(1-x^2)^3(1-x),x],{0,0,0,0,0,0,1,1},{1,55106}]*)


(* ::Input:: *)
(*Series[(x^6+x^9)/((1-x^2)^3(1-x^3)(1-x)),{x,0,20}]*)


(* ::Input:: *)
(*m=32012843503342576*)


(* ::Input:: *)
(*n=55106*)


(* ::Input:: *)
(*Binomial[6,3]*)


(* ::Input:: *)
(*(30+2*2+2*6+20+3*12+3*6)/12*)


(* ::Input:: *)
(*Series[(x^6+x^9)/((1-x)(1-x^2)(1-x^3)(1-x^4)),{x,0,20}]*)


(* ::Input:: *)
(*SeriesCoefficient[(x^6+x^9)/((1-x)(1-x^2)(1-x^3)(1-x^4)),{x,0,50000}]*)


(* ::Input:: *)
(*LinearRecurrence[Rest@-CoefficientList[(1-x)(1-x^2)(1-x^3)(1-x^4),x],{0,0,0,0,0,1,1,2,4,6},{1,55106}]*)


(* ::Input:: *)
(*Series[x^6/((1-x^4)(1-x^2)(1-x)),{x,0,20}]*)


(* ::Input:: *)
(*LinearRecurrence[Rest@-CoefficientList[(1-x^4)(1-x^2)(1-x),x],{0,0,0,0,0,1,1,2,2},{1,55106}]*)


(* ::Input:: *)
(*m=30;n=12*)


(* ::Input:: *)
(*(m+2Floor[n/6]+2Binomial[Floor[n/3],2]+Binomial[Floor[n/2],3]+3*2323833765120+3*189778176)/12*)


(* ::Chapter:: *)
(*Direct Congruence Calculation*)


(* ::Text:: *)
(*It turns out letting b <= d <= f, t >= 0 parameterizes the hexagons up to congruence exactly. (For t < 0, swap (a,d), (b,e), (c,f) as a 180 deg rotation.) *)
(*Parameterize d = b + y, f = d + z = b + y + z. Then we simply count solutions to a + b + c + d + e + f = 6b + 4y + 2z + 3t <= n,*)
(*equivalently the non-negative solutions to 6b' + 4y + 2z + 3t + s = n - 6. *)


(* ::Input:: *)
(*s=Series[x^6/((1-x)(1-x^2)(1-x^3)(1-x^4)(1-x^6)),{x,0,20}]*)


(* ::Input:: *)
(*cl=CoefficientList[(1-x)(1-x^2)(1-x^3)(1-x^4)(1-x^6),x]*)


(* ::Input:: *)
(*CoefficientList[s,x][[2;;16]]*)


(* ::Input:: *)
(*LinearRecurrence[Rest@-cl,CoefficientList[s,x],{2,n+1}]*)


(* ::InheritFromParent:: *)
(*Last[%]*)
