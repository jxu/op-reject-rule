/* segtree implementation
 * see python file for explanation
 */

#include <stdio.h>
#include <sys/param.h>

/* last row of tree ARR_START = 2 ** floor(log2(n)) */

#ifdef DEBUG
    #define N         5
    #define L_LO      0
    #define L_HI      6
    #define ARR_START 8
#else
    #define N         10000003
    #define L_LO      10000000
    #define L_HI      10200000
    #define ARR_START (1 << 23)
#endif

long long u[4*N], p[4*N], s[4*N], w[4*N];
int A[N], t[2*L_HI];


void update_seg(int j)
{
    int si = ARR_START + j;
    u[si] = A[j];
    p[si] = A[j];
    s[si] = A[j];
    w[si] = A[j];

    while (si > 1) 
    {
        int l = 2 * (si/2);
        int r = l + 1;
        u[si/2] = u[l] + u[r];
        p[si/2] = MAX(p[l], u[l] + p[r]);
        s[si/2] = MAX(s[r], s[l] + u[r]);
        w[si/2] = MAX(MAX(w[l], w[r]), s[l] + p[r]);

        si /= 2;
    }
}


int main()
{
    long long Mtotal = 0;

    /* precompute tribonacci numbers mod n */
    t[0] = 0; t[1] = 0; t[2] = 1;
    for (int k = 3; k < 2*L_HI; k++)
        t[k] = (t[k-1] + t[k-2] + t[k-3]) % N;

    for (int i = 1; i <= L_HI; i++)
    {
        /* array update */
        int j = t[2*i-2];
        A[j] += 2*t[2*i-1] - N + 1;

        if (i <= L_LO) continue;

        /* init segtree values */
        if (i == L_LO+1)
        {
            for (int m = 0; m < N; ++m)
                update_seg(m);
        }
        else
            update_seg(j);

        Mtotal += w[1];
   }

    printf("%lld\n", Mtotal);
}
