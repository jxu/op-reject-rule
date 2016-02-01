#include <iostream>

int l(const int n)
{
    int p = 1;
    long long i = n-2;

    for (i; i>=1; i-=1)
    {
        if (n%2 == 0 && i%2 != 1)
            continue;
        if (n%3 == 0 && (i%3 != 1 || i%3 != 2))
            continue;


        if (i*i % n == 1)
            return i;
    }

    return 1;




}

int main()
{
    long long s = 0;
    //for (int n=3; n<=100000; n++)
    //    s += l(n);
    std::cout << s << std::endl;
    return 0;
}
