#include "stdio.h"

#define N 18

char memo[1 << N];  // init to zero, meaning not calculated

long long pow_(int a, int b)
{
    long long x = 1;
    for (int i = 0; i < b; ++i)
        x *= a;
    return x;
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
        {
            s += pow_(9, __builtin_popcount(x));  
        }
    }
    printf("%lld\n", s);
}
