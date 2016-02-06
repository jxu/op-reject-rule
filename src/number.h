// Commonly used number related functions
#include <cmath>
#include <vector>
#include <iostream>

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

std::vector<int> sieve(int n)
{
    std::vector<bool> nums(n, 0);
    for (int i=2; i<sqrt(n)+1; i++)
    {
        if (nums[i] == 0)
        {
            for (int j=i*i; j<n; j+=i)
                nums[j] = 1;
        }
    }

    std::vector<int> result;
    for (int i=2; i<n; i++)
    {
        if (nums[i] == 0) result.push_back(i);
    }
    return result;
}

void print_vint(std::vector<int> v)
{
    for (int x : v)
        std::cout << x << ' ';
    std::cout << '\n';
}

#endif // NUMBER_H
