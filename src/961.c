#include "stdio.h"

#define N 18

char memo[1 << N];  // init to zero, meaning not calculated

// compute 9 ** popcount(x) with x's bits
long long popcount9(int x)
{
    long long t = 1;
    for (; x; x >>= 1)
        if (x & 1) t *= 9;
    return t;
}

int remove_bit(int x, int d)
{
    int lomask = (1 << d) - 1;
    int himask = (~lomask) << 1;
    return (x & lomask) | ((x & himask) >> 1);
}

char negamax(int x)
{
    if (x == 0) return -1;

    // non-zero means calculated
    if (memo[x]) return memo[x];

    for (int d = 0; (1 << d) <= x; ++d)
    {
        if (-negamax(remove_bit(x, d)) == 1)
            return memo[x] = 1; 
    }
    return memo[x] = -1; 
}

int main()
{
    long long s = 0;

    for (int x = 0; x < 1 << N; ++x)
    {
        if (negamax(x) == 1)
            s += popcount9(x);
    }
    printf("%lld\n", s);
}
