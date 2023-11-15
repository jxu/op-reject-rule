#include <stdio.h>
#include <math.h>

double e[1 << 12];

int main(void)
{
    for (int t = 0; t < 500; ++t)
    {
        for (int i = 1; i < (1 << 12); ++i) 
        {
            e[i] = 0;

            for (int x = 1; x <= 6; ++x) 
            {
                for (int y = 1; y <= 6; ++y)
                {
                    int ix = i ^ (1 << (x-1)); 
                    int iy = i ^ (1 << (y-1));
                    int ixy = i ^ (1 << (x+y-1));
                    
                    e[i] += (1 + fmin(fmin(e[ix], e[iy]), e[ixy])) / 36;
                }
            }

        }
        printf("%f\n", e[(1 << 12) - 1]);
    }
}