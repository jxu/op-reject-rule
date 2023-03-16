fun partition ([]   , l, r) = [[l, r]]
  | partition (x::xs, l, r) = partition (xs, x::l, r) @ 
                              partition (xs, l, x::r)

fun cartesian_product (x, y) = 
    let fun loop ([]    , _     ) = []
          | loop (x'::xs, []    ) = loop (xs, y) 
          | loop (x'::xs, y'::ys) = [x', y'] :: loop (x'::xs, ys)
    in loop (x, y) end

