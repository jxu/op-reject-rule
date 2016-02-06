// F(44) didn't fit in python memory and too lazy to rewrite python sieve
// more memory-efficient array

// Goldbach's conjecture: e = p + q for even e >= 4
// Odd numbers are form  p, p+2, p+q+3 x>=7, p+q+3+2 x>=9, p+q+3+2+2 x>=11, ...
// Even numbers are form 2, p+q x>=4, p+q+2 x>=6, p+q+2+2 x>=8, ...

#include <vector>
#include <iostream>
#include "number.h"

long long S(const int n)
{
    long long total_count = 0;
    std::vector<int> primes = sieve(n+1); // include n
    total_count += primes.size(); // k=1 prime

    for (size_t i=0; i<primes.size(); i++)
    {
        if (primes[i] != 2 && primes[i] + 2 <= n) // odd p+2
            total_count++;
    }

    if (n>2)
    {
        long long e = n/2 - 1;
        long long o = (n-1)/2 - 2;
        total_count += e*(e+1)/2; // sum even nums
        total_count += o*(o+1)/2; // sum odd nums
    }


    return total_count;
}

int main()
{
    std::cout << S(11) << std::endl;
    long long result = 0;
    int a = 0, b = 1;
    for (int i=0; i<=44; i++)
    {
        if (i >= 3)
        {
            std::cout << "S(" << a << ") " << S(a) << std::endl;
            result += S(a);
        }
        int c = a+b; a = b; b = c;
    }
    std::cout << result << std::endl;
    return 0;
}
