#include <stdio.h>
#include <stdbool.h>

#define D 10
#define PAR (1 << 5)
#define MOD 21
#define L 6
#define DEPTH 30

#define N 1000LL

const int RULE21[] = {1, 10, 16, 13, 4, 19};
const int DIGITS[L] = {0, 1, 3, 5, 7, 9};

// GNU extension
// -1 use to represent not done
long long dp[D][PAR][MOD][DEPTH] = 
    {[0 ... D-1][0 ... PAR-1][0 ... MOD-1][0 ... DEPTH-1] = -1};

long long f(int d, int par, int m21, int depth)
{
    if (dp[d][par][m21][depth] >= 0)
        return dp[d][par][m21][depth];

    if (depth == 0)
    {
        dp[d][par][m21][depth] = (d == 5 && par == 0b11111 && m21 == 0);
        return dp[d][par][m21][depth];
    }

    long long s = 0;

    for (int i = 0; i < L; ++i)
    {
        int d_new = DIGITS[i];
        if (d_new == 0 && d != 0)
            continue;
        
        int par_new = par ^ ((d_new!=0) * 1 << (d_new/2));
        int m21_new = (m21 + RULE21[depth%6] * d_new) % MOD;

        s += f(d_new, par_new, m21_new, depth-1);
    }
    dp[d][par][m21][depth] = s;
    return s;
}

void search(long long n, int d, int par, int m21, int depth)
{
    if (depth == 0)
        return;
    
    for (int i = 0; i < L; ++i)
    {
        int d_new = DIGITS[i];
        if (d_new == 0 && d != 0)
            continue;
        
        int par_new = par ^ ((d_new!=0) * 1 << (d_new/2));
        int m21_new = (m21 + RULE21[depth%6] * d_new) % MOD;

        long long node_sum = f(d_new, par_new, m21_new, depth-1);

        if (n <= node_sum)
        {
            if (d_new > 0)
                printf("%d", d_new);
            return search(n, d_new, par_new, m21_new, depth-1);
        }

        n -= node_sum;
    }
}

int main()
{
    search(N, 0, 0, 0, DEPTH);
}
