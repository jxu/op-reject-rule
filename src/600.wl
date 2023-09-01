(* ::Package:: *)

(* ::Text:: *)
(*Calculationsx+y*)


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


(* ::Input:: *)
(*Floor[n/6]*)
