// Use prefix sums to avoid recomputing row sums many times
// Other than that, O(n^3) brute force subtriangles (< 1 sec)
// Compile with gcc -Wall -O3 -o 150 150.c

#include <stdio.h>

#define TRI_SIZE 500500
#define ROWS 1000

#define MIN(a,b) (((a)<(b))?(a):(b))

int tri[TRI_SIZE];
int row_prefix[ROWS][ROWS];

size_t IX(int i, int j)
{
    return i*(i+1)/2 + j;
}

int main()
{
    int t = 0, min_tri = 1 << 30;

    for (int k = 0; k < TRI_SIZE; k++)
    {
        t = (615949*t + 797807) % (1<<20);
        tri[k] = t - (1<<19);
    }

    for (int i = 0; i < ROWS; i++)
    {
        row_prefix[i][0] = tri[IX(i,0)];
        for (int j = 1; j <= i; j++)
        {
            row_prefix[i][j] = row_prefix[i][j-1] + tri[IX(i,j)];
        }
    }

    for (int i = 0; i < ROWS; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            int upper_tri_sum = 0;
            for (int s = 0; i+s < ROWS; s++) // Try triangles of size s+1
            {
                upper_tri_sum += row_prefix[i+s][j+s];
                if (j > 0) upper_tri_sum -= row_prefix[i+s][j-1];
                min_tri = MIN(min_tri, upper_tri_sum);
            }
        }
    }

    printf("%d \n", min_tri);


    return 0;
}
