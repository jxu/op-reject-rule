#include "stdio.h"

#define N 600000000

unsigned int t[(N+1)/2];

unsigned int tots(unsigned int i) 
{
    unsigned int ih = i / 2;
    if (i % 2) 
        return t[i/2];
    else
        return (ih % 2) ? t[ih/2] : 2 * tots(ih);
}

int main(void) 
{
    for (unsigned int i = 1; i <= N; i += 2) 
        t[i/2] = i;

    for (unsigned int p = 3; p <= N; p += 2)
    {
        if (p == t[p/2]) 
        {
            for (int k = p; k <= N; k += 2*p) 
                t[k/2] -= t[k/2] / p;
        }
    }

    long long s = 0;
    for (unsigned int i=1; i<=N; ++i) 
        s += tots(i);

    printf("%lld\n", s);
}
