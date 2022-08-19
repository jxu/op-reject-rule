n = 10^16;
ymax = Floor[Sqrt[4 *n/163]];
s = -1;
Print[ProgressIndicator[Dynamic[y], {-ymax, ymax}]];
For[y = -ymax, y <= ymax, y++,
  sqrtdisc = Sqrt[4*n - 163*y^2];
  xmin = Ceiling[(-sqrtdisc - y)/2];
  xmax = Floor[(sqrtdisc - y)/2];
  s += xmax - xmin + 1
  ];
s