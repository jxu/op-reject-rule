Expand[Sum[x^((k (1 + k))/2), {k, 0, 10}]^3]

Sum[x^((k (1 + k))/2), {k, 0, Infinity}]
(* EllipticTheta[2,0,Sqrt[x]]/(2 x^(1/8)) *)

(* Research: 
https://arxiv.org/abs/1601.06378
http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.527.8724&rep=rep1&type=pdf *)
