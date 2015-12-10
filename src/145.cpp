#include <iostream>

inline bool reversible(int n)
{
    if (n % 10 == 0) return false;
    int m = n, r = 0, d;
    while (m)
    {
        d = m % 10;
        r = 10*r + d;
        m /= 10;
    }

    n = r + n;
    while (n)
    {
        if (n % 2 == 0)
            return false;
        n /= 10;
    }
    return true;
}

int main()
{
    int s = 0;
    for (int i=0; i<100000000; i++)
    {
        if (reversible(i)) s++;
    }
    std::cout << s << std::endl;
    return 0;
}
