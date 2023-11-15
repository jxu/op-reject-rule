#include <stdio.h>
#include <math.h>

double R(int n)
{
    double e[1000] = {0};
    for (int t=0; t<50; ++t)
    {
        for (int i=1; i<n; ++i)
        {
            e[i] = 1 + fmin(5*i%n/(5.*i) * e[5*i%n],
                            6*i%n/(6.*i) * e[6*i%n]);
        }
    }
    return e[1];
}


int main(void)
{
    double s = 0;
    for (int k=2; k<=1000; ++k)
        s += R(k);
    printf("%f\n", s);
}