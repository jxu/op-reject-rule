/* Endagorion idea: for given y, maintain x range of solutions and
 * adjust [xl, xr] for consecutive y
 * Works since ranges are overlapping (not disjoint) for consecutive y
 * No quadratic equation solving or floating point 
 */

#include <stdbool.h>
#include <stdio.h>

#define N 10

bool in_ellipse(long long x, long long y)
{
    printf("%lld %lld\n", x, x*x + x*y + 41*y*y);
    return x*x + x*y + 41*y*y <= N;
}

/* Finds new [xl, xr] range for given y
 * Return number of x points in range, if 0 then ignore updated xl and xr
 * Requires passed in [xl, xr] to overlap with returned new range,
 * that is at least one new endpoint is within old range
 */
long long adjust_range(long long *xl, long long *xr, long long y)
{
    while (in_ellipse(*xr, y)) {
        ++*xr;
    }
    --*xr; 
    return *xr;
}

int main() 
{
    long long xl = 0, xr = 0;
    printf("%lld\n", adjust_range(&xl, &xr, 0));
    return 0;
}
