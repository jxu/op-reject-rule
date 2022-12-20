/* Translation of silly python near version. Runs in under 1 sec */

#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include <sys/param.h>  /* MIN and MAX */

#define B 10
#define k 14

double complex Px[k];
double complex Py[k];

int compare_real(const void* a, const void* b)
{
    double ra = creal(*(const double complex*)a);
    double rb = creal(*(const double complex*)b);
    return (ra > rb) - (ra < rb);
}

int compare_imag(const void* a, const void* b)
{
    double ra = cimag(*(const double complex*)a);
    double rb = cimag(*(const double complex*)b);
    return (ra > rb) - (ra < rb);
}

double dist(const double complex p0, const double complex p1) 
{
    return cabs(p0 - p1);
}

/* take in Px, Py, L, n, return in buffer Px_left and Py_right, n_left vals */
void left_half(const double complex Px[], 
               double complex Px_left,            
               const double complex Py[],
               double complex Py_left,
               const size_t n,
               size_t* n_left,
               const double L)
{
    

}

double closest_pair(const double complex Px[], const double complex Py[],
        const size_t n)
{
    return 0;
}

int main()
{
    long long s = 290797;

    for (int n=0; n < 2*k; ++n)
    {
        Px[n/2] += (double complex)s * (n%2 ? I : 1);
        Py[n/2] = Px[n/2];
        s = (s * s) % 50515093;
    }

    qsort(Px, k, sizeof(double complex), compare_real);
    qsort(Py, k, sizeof(double complex), compare_imag);

    double D = 1e9;
    for (int i=0; i<k; ++i)
    {
        printf("%f%+f\n", creal(Py[i]), cimag(Py[i]));
        for (int j = MAX(0, i-B); j < MIN(k, i+B); ++j)
        {
            if (i == j) continue;
            D = MIN(D, cabs(Px[i] - Px[j]));
        }
    }

    printf("%.9f\n", D);

    return 0;
}
