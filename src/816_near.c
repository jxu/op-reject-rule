/* Translation of silly python near version. Runs in under 1 sec */

#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include <sys/param.h>  /* MIN and MAX */

#define B 10
#define k 2000000

double complex P[k];

int compare_complex(const void* a, const void* b)
{
    double ra = creal(*(const double complex*)a);
    double rb = creal(*(const double complex*)b);
    return (ra > rb) - (ra < rb);
}

int main()
{
    long long s = 290797;

    for (int n=0; n < 2*k; ++n)
    {
        P[n/2] += (double complex)s * (n%2 ? I : 1);
        s = (s * s) % 50515093;
    }

    qsort(P, k, sizeof(double complex), compare_complex);

    double D = 1e9;
    for (int i=0; i<k; ++i)
    {
        /* printf("%f%+f\n", creal(P[i]), cimag(P[i])); */
        for (int j = MAX(0, i-B); j < MIN(k, i+B); ++j)
        {
            if (i == j) continue;
            D = MIN(D, cabs(P[i] - P[j]));
        }
    }

    printf("%.9f\n", D);

    return 0;
}
