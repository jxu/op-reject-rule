#include <stdio.h>

int gcd(int a, int b)
{
    while (b)
    {
        int c = a % b;
        a = b;
        b = c;
    }
    return a;
}

int phi(int n)
{
    int x = 0;
    for (int i=1; i<=n; i++)
    {
        if (gcd(n, i) == 1)
            x++;
    }
    return x;
}

int main()
{
    int sum = 0;
    for (int i=1; i<19000; i++) // Change this so it runs in 10 seconds
        sum += phi(i);
    
    printf("%d\n", sum);
    return 0;
}
