/* Endagorion idea: for given y, maintain x range of solutions and
 * adjust [xl, xr] for consecutive y
 * Works since ranges are overlapping (not disjoint) for consecutive y
 * No quadratic equation solving or floating point 
 */

#include <stdbool.h>
#include <stdio.h>

#define N 1e16
#define ll long long

bool in_ellipse(ll x, ll y)
{
    return x*x + x*y + 41*y*y <= N;
}

/* Finds new [xl, xr] range for given y
 * Return number of x points in range, if 0 then ignore updated xl and xr
 * Requires passed in [xl, xr] to overlap with returned new range,
 * that is at least one new endpoint is within old range
 */
ll adjust_range(ll *xl, ll *xr, ll y)
{
    while (in_ellipse(*xr, y)) 
        ++*xr;
    --*xr;
    
    while (!in_ellipse(*xr, y))
    {
        --*xr;
        if (*xr < *xl) return 0;
    }

    while (in_ellipse(*xl, y))
        --*xl;
    ++*xl;
    
    while (!in_ellipse(*xl, y))
        ++*xl;

    return *xr - *xl + 1;
}

int main() 
{
    ll s = -1, xl = 0, xr = 0, y = 0, m;
    while ((m = adjust_range(&xl, &xr, y)))
    {
        s += m; 
        ++y;
    }
    
    y = -1; xl = 0; xr = 0; 
    while ((m = adjust_range(&xl, &xr, y)))
    {
        s += m;
        --y;
    }

    printf("%lld\n", s);
    return 0;
}
