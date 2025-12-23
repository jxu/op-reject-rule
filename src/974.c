#include <stdio.h>

#define D 10
#define PAR (1 << 5)
#define MOD 21
#define DEPTH 30

#define N 10000000000000000LL

const int RULE21[6] = {1, 10, 16, 13, 4, 19};
long long dp[DEPTH][D][PAR][MOD];

void search(long long n, int d, int par, int m21, int depth)
{
    if (depth == 0)
        return;
    
    for (int d_new = 0; d_new < D; ++d_new)
    {
        if (d_new > 0 && d_new % 2 == 0)
            continue;

        if (d_new == 0 && d != 0)
            continue;
        
        int par_new = par ^ ((d_new!=0) * 1 << (d_new/2));
        int m21_new = (m21 + RULE21[depth%6] * d_new) % MOD;

        long long node_sum = dp[depth-1][d_new][par_new][m21_new];

        if (n <= node_sum)
        {
            if (d_new > 0)
                printf("%d", d_new);
            search(n, d_new, par_new, m21_new, depth-1);
            return; // ISO C forbids return expression for void
        }

        n -= node_sum;
    }
}

int main()
{
    // bottom-up DP instead of memoize as silly experiment
    // does extra work by filling out every value
    for (int depth = 0; depth < DEPTH; ++depth)
    {
        for (int d = 0; d < D; ++d)
        {
            for (int par = 0; par < PAR; ++par)
            {
                for (int m21 = 0; m21 < MOD; ++m21)
                {
                    if (depth == 0)
                    {
                        dp[depth][d][par][m21] = 
                            (d == 5 && par == 0x1F && m21 == 0);
                        continue;
                    }

                    for (int d_new = 0; d_new < D; ++d_new)
                    {
                        // skip nonzero evens, use zero and odds
                        if (d_new > 0 && d_new % 2 == 0)
                            continue;
                        
                        // only leading zeros
                        if (d_new == 0 && d != 0)
                            continue;
                        
                        int par_new = par ^ ((d_new!=0) * 1 << (d_new/2));
                        int m21_new = (m21 + RULE21[depth%6] * d_new) % MOD;

                        dp[depth][d][par][m21] += 
                            dp[depth-1][d_new][par_new][m21_new];
                    }
                    
                }
            }
        }
    }

    search(N, 0, 0, 0, DEPTH);
}
