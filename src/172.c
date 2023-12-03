/* EGF: x^18/18! coefficient of (1 + x + x^2/2 + x^3/6)^10 */

#include <stdio.h>

#define LEN 18
#define M 4

long long P[LEN+1] = {6402373705728000}; /* polynomial 18! x^0 */
const long long DEN[M] = {1, 1, 2, 6};

int main(void)
{
    for (int d=0; d<10; ++d)
    {
        long long Q[LEN+1] = {0};
        for (int i=0; i<=LEN; ++i)
        {
            for (int j=0; j<M; ++j)
            {
                if (i+j <= LEN)
                    Q[i+j] += P[i] / DEN[j];
            }
        }

        for (int i=0; i<=LEN; ++i)
            P[i] = Q[i];
    }

    printf("%lld\n", P[LEN] * 9 / 10);
}
