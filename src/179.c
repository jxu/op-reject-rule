#include <stdio.h>

#define N 10000000

int sigma[N+1];

int main()
{
    for (int n = 1; n <= N; n++)
    {
        for (int i = n; i <= N; i += n)
            sigma[i]++;
    }

    int s = 0;
    for (int n = 2; n < N; n++)
        if (sigma[n] == sigma[n+1]) 
            s++;

    printf("%d\n", s);
}