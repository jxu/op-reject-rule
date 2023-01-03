#include <stdio.h>
#include <math.h>

double s(double r)
{
    double x = 6e11;
    for (int k=1; k<=5000; ++k)
        x += (900 - 3*k) * pow(r, k-1);
    return x;
}

double ds(double r)
{
    double x = 0;
    for (int k=1; k<=5000; ++k)
        x += (900 - 3*k) * (k-1) * pow(r, k-2);
    return x;
}

int main(void)
{
    double x = 1.1;
    for (int i=0; i<1000; ++i)
        x -= s(x) / ds(x);

    printf("%0.12f\n", x);
}
