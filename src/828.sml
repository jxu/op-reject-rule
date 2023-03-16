fun partition ([],    l, r) = [[l, r]]
  | partition (x::xs, l, r) = partition (xs, x::l, r) @ 
                              partition (xs, l, x::r)
