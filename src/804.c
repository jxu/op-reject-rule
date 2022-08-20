#include <math.h>
#include <stdio.h>

long long T(long long N) 
{
    long long y_max = floor(sqrt(4*N / 163));
    long long s = -1;

    for (long long y = -y_max; y <= y_max; ++y)
    {
        double sqrt_disc = sqrt(4*N - 163*y*y);
        long long x_min = ceil((- sqrt_disc - y) / 2);
        long long x_max = floor((sqrt_disc - y) / 2);
        s += x_max - x_min + 1;
    }
    return s;
}

int main() 
{
    printf("%lld\n", T(1e16));
    return 0;
}
