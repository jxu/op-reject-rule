/* Slower than python version, I think due to inefficient qsort */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <sys/param.h>

#ifdef DEBUG
    #define N       200
    #define K_MAX   284
#else
    #define N       10000
    #define K_MAX   14210 // int(N * log(M_PI + 1))
#endif

#define PAIRS_MAX ((K_MAX)*(K_MAX+1)/2)

typedef struct 
{
    double val;
    int a;
    int b;
} ab_pair;

double fn[K_MAX];
ab_pair pairs[PAIRS_MAX]; 

int compare(const void* x1, const void* x2)
{
    ab_pair p1 = *((ab_pair*)x1);
    ab_pair p2 = *((ab_pair*)x2);
    return (p1.val > p2.val) - (p1.val < p2.val);
}

int main()
{
    for (int k = 0; k < K_MAX; ++k)
        fn[k] = exp((double)k/N) - 1;

    int n_pairs = 0;
    for (int a = 0; a < K_MAX; ++a)
    {
        for (int b = a; b < K_MAX; ++b)
        {
            if (fn[a] + fn[b] > M_PI) break;
            pairs[n_pairs].val = fn[a] + fn[b];
            pairs[n_pairs].a = a;
            pairs[n_pairs].b = b;
            ++n_pairs;
        }
    }

    printf("%d pairs\n", n_pairs);
    qsort(pairs, n_pairs, sizeof(ab_pair), compare);

    double best_error = 1e-7;
    int best_g;
    int i = 0, j = n_pairs-1;

    while (i <= j)
    {
        double error = pairs[i].val + pairs[j].val - M_PI;

        if (fabs(error) < best_error)
        {
            best_error = fabs(error);
            int a = pairs[i].a, b = pairs[i].b,
                c = pairs[j].a, d = pairs[j].b;

            best_g = a*a + b*b + c*c + d*d;

            printf("%d %d %d %d %0.16f\n", a, b, c, d, error);
        }

        if (error > 0) j -= 1;
        else i += 1;
    }

    printf("%d\n", best_g);
}
