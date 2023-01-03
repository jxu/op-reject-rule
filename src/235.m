(* Credit: OggyWan *)
NSolve[Sum[(900 - 3k) r^(k-1), {k, 1, 5000}] == -600000000000, r, Reals, WorkingPrecision -> 13]