Select[Range[10^6, 1.1*10^6], # - PrimePi[#] >= 10^6 &, 1]
Select[Range[2*10^6], PrimeOmega[#] >= 3 &][[10^6]]
Select[Range[2.5*10^6], PrimeOmega[#] >= 4 &][[10^6]]