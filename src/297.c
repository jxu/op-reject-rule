/* Same as python, but precompute Z[fib[i]] as ZF */

#include <stdio.h>

#define FMAX 90

long long fib[FMAX];
long long ZF[FMAX];

long long Z(long long N)
{
    if (N <= 1) return 0;
    int i;
    for (i = FMAX-1; fib[i] >= N; --i) ;
    return N - fib[i] + Z(N - fib[i]) + ZF[i];
}

int main() 
{
    fib[0] = 0; fib[1] = 1;
    for (int i = 2; i < FMAX; ++i)
        fib[i] = fib[i-1] + fib[i-2];

    ZF[0] = 0; ZF[1] = 0;
    for (int i = 1; i < FMAX-1; ++i) 
        ZF[i+1] = fib[i-1] + ZF[i] + ZF[i-1];

    printf("%lld\n", Z(1e17));
}

