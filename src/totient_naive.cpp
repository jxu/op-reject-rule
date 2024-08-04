#include <iostream>
using namespace std;

int gcd(int a, int b)
{
    while (b != 0)
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
    unsigned int sum = 0;
    for (int i=1; i<19000; i++) // Change this so it runs in 10 seconds
    {
        sum += phi(i);
    }
        cout << sum << endl;
        return 0;
}
