// q*d + r = n;  must be r,d,q or r,q,d
// (d^3)/r + r = a^2

#include <iostream>
#include "number.h"
#include <cmath>

const long long LIMIT = pow(10, 12);
const int RATIO_LIMIT = 15;

int main()
{
    long long s = 0;
    for (long long d=1; d<int(sqrt(LIMIT)); d++)
    {
        for (int r=d-1; r>=1; r--)
        {
            long long n = d*d*d/r + r;
            if (n >= LIMIT || d/r > RATIO_LIMIT) break;
            if (d*d*d % r == 0 && is_square(n))
            {
                s += n;
                std::cout << d << '\t' << r << '\t' << float(d)/r << '\t' << sqrt(n) << std::endl;
            }
        }
    }
    std::cout << s << std::endl;
    return 0;
}
