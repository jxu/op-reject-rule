(* ::Package:: *)

(* ::Title:: *)
(*Generatingfunctionology*)


(* ::Text:: *)
(*Key observation: Equiangular hexagons are fully determined by their sides (a,b,c,d,e,f), with constraints a + b = d + e, b + c = e + f, c + d = f + a (last is redundant). *)
(*The invariant is t = a - d = e - b = c - f, giving the parameterization a = d + t, e = b + t, c = f + t.*)
(**)


(* ::Chapter:: *)
(*With Burnside's Lemma*)


(* ::Section:: *)
(*Hexagons without considering congruence (identity action)*)


(* ::Text:: *)
(*Case t > 0: a = d + t, e = b + t, c = f + t*)
(*a + b + c + d + e + f = 2b + 2d + 2f + 3t <= N (all integers > 0)*)
(*2b' + 2d' + 2f' + 3t' + s = N - 9 (all integers >= 0)*)
(*GF: x^9 / ((1-x^2)^3 (1-x^3) (1-x)) *)
(**)
(*Case t < 0: symmetric *)
(**)
(*Case t = 0: a = d, b = e, c = f*)
(*2a + 2b + 2c <= N (all integers > 0)*)
(*2a' + 2b' + 2c' + s = N - 6 (all integers >= 0)*)
(*GF: x^6 / ((1-x^2)^3(1-x))*)
(**)
(*Final GF = (x^6 + x^9) / ((1-x^2)^3 (1-x^3) (1-x)) *)


(* ::Input:: *)
(*n=55106;*)
(*ri=Simplify[SeriesCoefficient[(x^6+x^9)/((1-x^2)^3(1-x^3)(1-x)),{x,0,m}]/.m->n]*)


(* ::Section:: *)
(*\[PlusMinus]60\[Degree] rotation*)


(* ::Text:: *)
(*a = b = c = d = e = f*)
(*Count n // 6*)


(* ::Input:: *)
(*r60=Floor[n/6]*)


(* ::Section:: *)
(*\[PlusMinus]120\[Degree] rotation*)


(* ::Text:: *)
(*a = c = e, b = d = f*)
(*Count solutions to 3 a + 3 b <= N (ints > 0), equiv. solutions to a + b + s = N//3 + 1 with stars-and-bars *)


(* ::Input:: *)
(*r120=Binomial[Floor[n/3],2]*)


(* ::Section:: *)
(*180\[Degree] rotation*)


(* ::Text:: *)
(*a = d, b = e, c = f*)
(*Count solutions to 2a + 2b + 2c <= N, equiv a + b + c + s = N//2 + 1 *)


(* ::Input:: *)
(*r180=Binomial[Floor[n/2],3]*)


(* ::Section:: *)
(*Reflection through vertex*)


(* ::Text:: *)
(*a = b = d = e, c = f*)
(*Positive solutions to 4a + 2b <= N, equiv nonnegative solutions 4a' + 2c' + s = N-6*)
(*GF: x^6 / ((1-x^4)(1-x^2)(1-x))*)


(* ::Input:: *)
(*sv=Simplify[SeriesCoefficient[x^6/((1-x^4)(1-x^2)(1-x)),{x,0,m}]/.m->n]*)


(* ::Section:: *)
(*Reflection through side*)


(* ::Text:: *)
(*c = e, b = f, a+b = d+e (redundant a+f = c+d)*)
(**)
(*Case t > 0: a = d + t, e = c = b+t*)
(*Positive solutions to 2d + 4b + 3t <= N*)
(*Nonnegative solutions to 2d' + 4b' + 3t' + s = N-9*)
(*GF: x^9 / ((1-x)(1-x^2)(1-x^3)(1-x^4)) *)
(**)
(*Case t = 0: a = d, e = b = c = f. Same GF as reflection thru vertex*)
(**)
(*Final GF: (x^6 + x^9) / ((1-x)(1-x^2)(1-x^3)(1-x^4)) *)


(* ::Input:: *)
(*ss=Simplify[SeriesCoefficient[(x^6+x^9)/((1-x)(1-x^2)(1-x^3)(1-x^4)),{x,0,m}]/.m->n]*)


(* ::Section:: *)
(*The magic formula*)


(* ::Input:: *)
(*(ri+2r60+2r120+r180+3ss+3sv)/12*)


(* ::Chapter:: *)
(*Direct Congruence Calculation*)


(* ::Text:: *)
(*It turns out letting b <= d <= f, t >= 0 parameterizes the hexagons up to congruence exactly. (For t < 0, swap (a,d), (b,e), (c,f) as a 180 deg rotation.) *)
(*Parameterize d = b + y, f = d + z = b + y + z. Then we simply count solutions to a + b + c + d + e + f = 6b + 4y + 2z + 3t <= n,*)
(*equivalently the non-negative solutions to 6b' + 4y + 2z + 3t + s = n - 6. *)


(* ::Input:: *)
(*s=Series[x^6/((1-x)(1-x^2)(1-x^3)(1-x^4)(1-x^6)),{x,0,20}]*)


(* ::Input:: *)
(*Simplify[SeriesCoefficient[x^6/((1-x)(1-x^2)(1-x^3)(1-x^4)(1-x^6)),{x,0,m}]/.m->n]*)


(* ::Text:: *)
(*How to evaluate as linear recurrence:*)


(* ::Input:: *)
(*cl=CoefficientList[(1-x)(1-x^2)(1-x^3)(1-x^4)(1-x^6),x]*)


(* ::Input:: *)
(*CoefficientList[s,x][[2;;16]]*)


(* ::Input:: *)
(*LinearRecurrence[Rest@-cl,CoefficientList[s,x],{2,n+1}]*)


(* ::InheritFromParent:: *)
(**)


(* ::Input:: *)
(*Last[%]*)
