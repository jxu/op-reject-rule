/* Small variation on node values,
 * because the nodes along the way are just the first ith bits of d
 * Can also use a set data structure to avoid conditional in range,
 * since for the zero bits in d, d & mask is the same (credit: hkmt)
 */
#include <stdio.h>

long long f(long long n, long long k)
{
    long long s = n;
    long long d = n - k;
    for (int i = 0; i < 64; ++i)
    {
        if ((d >> i) & 1)
        {
            long long mask = (2ll << i) - 1;
            s += n - (d & mask);
        }
    }
    return s;
}

int main(void)
{
    printf("%lld\n", f(100000000000000000, 16677181699666569));
}