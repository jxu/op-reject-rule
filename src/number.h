// Commonly used number related functions
#include <cmath>
#ifndef NUMBER_H
#define NUMBER_H

bool is_square(int n)
{
    if (n < 0) return false;
    int root = round(sqrt(n));
    return n == root * root;
}

bool is_square(long long n)
{
    if (n < 0) return false;
    long long root = round(sqrt(n));
    return n == root * root;
}

int gcd(int a, int b)
{
    while (b)
    {
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}

long long gcd(long long a, long long b)
{
    while (b)
    {
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}

#endif // NUMBER_H
