/* sqrt decomposition implementation
 * see python file for explanation
 */

#include <stdio.h>
#include <sys/param.h>

/* SEGLEN = floor(sqrt(N)), NSEG = ceil(N / SEGLEN) */

/*
#define N      5
#define L_LO   0
#define L_HI   6
#define SEGLEN 2
#define NSEG   3
*/

#define N      10000003
#define L_LO   10000000
#define L_HI   10200000
#define SEGLEN 3162
#define NSEG   3163

long long u[NSEG], p[NSEG], s[NSEG], w[NSEG];
int A[N], t[2*L_HI];


void update_seg(int si)
{
    long long cur_p = 0, cur_s = 0, cur_w = 0;
    u[si] = 0; p[si] = 0; s[si] = 0; w[si] = 0;

    int min_i = si*SEGLEN;
    int max_i = MIN((si+1)*SEGLEN, N);

    for (int i = min_i; i < max_i; i++)
    {
        int ri = (max_i - 1) - (i - min_i);
        u[si] += A[i];

        cur_p += A[i];
        p[si] = MAX(p[si], cur_p);

        cur_s += A[ri];
        s[si] = MAX(s[si], cur_s);

        cur_w = MAX(0, cur_w + A[i]);
        w[si] = MAX(w[si], cur_w);
    }
}


int main()
{
    long long Mtotal = 0;

    /* precompute tribonacci numbers mod n */
    t[0] = 0; t[1] = 0; t[2] = 1;
    for (int k = 3; k < 2*L_HI; k++)
    {
        t[k] = (t[k-1] + t[k-2] + t[k-3]) % N;
    }

    for (int i = 1; i <= L_HI; i++)
    {
        /* array update */
        int j = t[2*i-2];
        A[j] += 2*t[2*i-1] - N + 1;

        if (i <= L_LO) continue;

        if (i == L_LO+1)
        {
            for (int si = 0; si < NSEG; si++)
                update_seg(si);
        }

        /* update segment and compute M_i */
        int si = j / SEGLEN;
        update_seg(si);

        long long M = 0, msum = 0, msump;

        for (int si = 0; si < NSEG; si++)
        {
            msum = MAX(s[si], msum + u[si]);
            msump = msum + (si+1 < NSEG ? p[si+1] : 0);
            M = MAX(M, MAX(msump, w[si]));
        }
        Mtotal += M;
    }

    printf("%lld\n", Mtotal);
}
