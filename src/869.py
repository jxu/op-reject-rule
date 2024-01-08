from number import sieve
from functools import cache
from collections import Counter
from dataclasses import dataclass

# this is supposed to be more efficient than char strings like "0011" but
# it's not even that much faster. for fun
@dataclass
class Bitstring:
    val: int
    nbits: int

    def __hash__(self):
        return hash((self.val, self.nbits))

    def __repr__(self):  # prettier binary string output
        s = format(self.val, 'b').zfill(self.nbits) if self.nbits else '_'
        return f"<Bitstring {s}>"


suf = Counter()
primes = sieve(10**8)
pb = set()
for p in primes:
    bl = p.bit_length()
    pb.add(Bitstring(p, bl))  # p bitstring

    # add to counter p's suffixes
    for i in range(bl+1):
        mask = (1 << i) - 1
        suf[Bitstring(p & mask, i)] += 1


@cache
def E(x : Bitstring) -> float:
    """Maximized expected points given player knows lsb of prime x."""
    total = suf[x] - (x in pb)
    if total == 0: return 0

    x0 = Bitstring(x.val, x.nbits+1)
    x1 = Bitstring(x.val | (1 << x.nbits), x.nbits+1)

    p0 = (x0 in pb) / total
    p0m = (suf[x0] - (x0 in pb)) / total
    p1 = (x1 in pb) / total
    p1m = (suf[x1] - (x1 in pb)) / total

    e0 = p0 + p0m * (1 + E(x0)) + p1m * E(x1)
    e1 = p1 + p1m * (1 + E(x1)) + p0m * E(x0)

    print(x, e0, e1)
    return max(e0, e1)


print(round(E(Bitstring(0, 0)),8))