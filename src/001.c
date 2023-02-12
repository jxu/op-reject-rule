// simple C version
#include <stdio.h>

int main() 
{
    unsigned s = 0;
    for (unsigned n = 0; n < 1000; ++n) 
    {
        if (n % 3 == 0 || n % 5 == 0)
            s += n;
    }

    printf("%d\n", s);
}

