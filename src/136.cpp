#include <iostream>
#include <algorithm>

const int MAX_N = 50000000;
char d[MAX_N+1];

int main()
{
    for (int y=1; y<=MAX_N; y++)
    {
        for (int a=y/4; a<y && y*(4*a-y) <= MAX_N; a++)
        {
            if (4*a-y > 0) d[y*(4*a-y)]++;
        }
    }
    std::cout << std::count(d, d+MAX_N+1, 1) << std::endl;
    return 0;
}
