#include <cmath>
#include <iostream>
#include <unordered_set>
#include <numeric>

bool is_square(long n)
{
    long r = round(sqrt(n));
    return (r * r == n);
}

int main()
{
    const long N = 1'000'000'000'000;
    std::unordered_set<long> s;

    for (long r = 1; r + r*r < N; ++r) // more flexible for loop cond
    {
        int inc = (r % 4) ? 2 : 1;
        for (long c = 1; c * c <= r; c += inc)
        {
            if (r % (c*c)) continue; // only consider c^2 divides r
            for (long b = c + 1; ; ++b)
            {
                // Could put these as comma expressions in the cond,
                // but that's confusing
                long d = b * (r / c);
                long q = d * b / c;
                long n = d * q + r;
                if (n >= N) break;

                if (is_square(n))
                {
                    std::cout << r << " " << d << " " << q << " ";
                    std::cout << n << '\n';
                    s.insert(n);
                }
            }
        }
    }
    std::cout << std::accumulate(s.begin(), s.end(), 0L) << '\n';
}
