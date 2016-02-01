#include <iostream>
#include "number.h"

int P(long long N)
{
    int pt = 0;
    for (long long m=1; m*m <= N; m++)
    {
        for (long long n=m%2+1; n<m && m*m + n*n <= N; n+=2)
        {
            //long long a = m*m - n*n;
            //long long b = 2*m*n;
            //long long c = m*m + n*n;
            //std::cout << a << ' ' << b << ' ' << c << std::endl;
            if (gcd(m, n) == 1)
                pt++;
        }
    }
    return pt;
}

int main()
{
    std::cout << P(3141592653589) << std::endl;
    return 0;
}
