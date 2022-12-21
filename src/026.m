MaximalBy[
 Table[{d,
   If[Mod[d, 2] == 0 || Mod[d, 5] == 0, 0,
    MultiplicativeOrder[10, d]]},
    {d, 2, 1000}],
 Last]