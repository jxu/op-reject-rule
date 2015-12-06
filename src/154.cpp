#include <iostream>

int fact_pow(int f, int p)
{
    int s = 0;
    int x = p;
    while (f >= x)
    {
        s += f / x;
        x *= p;
    }
    return s;
}

int main()
{
    int fact_pow2[200001], fact_pow5[200001];
    for (int i=0; i<=200000; i++)
    {
        fact_pow2[i] = fact_pow(i, 2);
        fact_pow5[i] = fact_pow(i, 5);
    }

    int c = 0;
    int n2 = fact_pow2[200000];
    int n5 = fact_pow5[200000];

    for (int i=0; i<=200000; i++) // Brute force everyday
    {
        for (int j=0; j<=200000-i; j++)
        {
            int k = 200000-i-j;
            int ijk2 = fact_pow2[i] + fact_pow2[j] + fact_pow2[k];
            int ijk5 = fact_pow5[i] + fact_pow5[j] + fact_pow5[k];
            if (n2 - ijk2 >= 12 && n5 - ijk5 >= 12) c++;  // Nice
        }
    }
    std::cout << c << std::endl;
    return 0;
}
