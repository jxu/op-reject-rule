// Use prefix sums to avoid recomputing row sums many times
// Other than that, O(n^3) brute force subtriangles (< 1 sec)
// Compile with gcc -Wall -O3 -o 150 150.c

#include <stdio.h>

#define ROWS 1000
#define MIN(a,b) (((a)<(b))?(a):(b))

int row_prefix[ROWS][ROWS];

int main()
{
    int t = 0, min_tri = 1 << 30;

    for (int i = 0; i < ROWS; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            // Save space by not storing triangle explicitly
            t = (615949*t + 797807) % (1<<20);
            row_prefix[i][j] = t - (1<<19);
            if (j > 0) row_prefix[i][j] += row_prefix[i][j-1];
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
