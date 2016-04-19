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
    // Generate combos (i, j, k) with i <= j <= k
    for (int i=0; i<=200000/3; i++)
    {
        for (int j=i; j<=(200000-i)/2; j++) // i <= j <= 200000-i-j
        {
            int k = 200000-i-j;
            int ijk2 = fact_pow2[i] + fact_pow2[j] + fact_pow2[k];
            int ijk5 = fact_pow5[i] + fact_pow5[j] + fact_pow5[k];
            if ((fact_pow2[200000]-ijk2 >= 12) && (fact_pow5[200000]-ijk5 >= 12))
            {
                // Permutations
                if (i==j && j==k) c += 1;
                else if ((i==j && j<k) || (i<j && j==k)) c += 3;
                else c += 6; // i < j < k
            }
        }
    }
    std::cout << c << std::endl;
    return 0;
}
