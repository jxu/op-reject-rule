#include <stdio.h>

int main() 
{
    unsigned n = 0, s = 0, c3 = 0, c5 = 0;
    do
    {
        ++n;
        ++c3;
        ++c5;
        if (c3 == 3 || c5 == 5)
        {
            if (c3 == 3) 
                c3 = 0;
            if (c5 == 5)
                c5 = 0;
            s += n;
            
        }
    }
    while (n != 999);

    printf("%d\n", s);
}

