#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define N 1 << 27

bool s[N];

int xor_product(int x, int y) 
{
    int r = 0;
    while (y) 
    {
        if (y & 1) r ^= x;
        x <<= 1; y >>= 1;
    }
    return r;
}


int main()
{
    memset(s, false, sizeof(s));
    for (int i=2; i<N; ++i) 
    {
        if (!s[i]) 
        {
            for (int j=2; j<N; ++j)
            {
                int xp = xor_product(i, j);
                if (xp >= 2*N) break;
                if (xp < N) s[xp] = true;
            }
        }
    }

    int t = 0;
    for (int i=2; i<N; ++i)
    {
        if (!s[i]) ++t;
        if (t == 5000000) 
        {
            printf("%d\n", i);
            break;
        }
    }
}
