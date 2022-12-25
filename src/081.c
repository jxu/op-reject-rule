/* Exercise in reading files and working with arrays */
#include <stdio.h>
#include <sys/param.h>

#define N 80 

int matrix[N][N];
int path[N][N];

int main() 
{
    FILE *fp = fopen("p081_matrix.txt", "r");
    
    for (int i=0; i<N; ++i) 
    {
        for (int j=0; j<N; ++j) 
        {
            fscanf(fp, "%d,", &matrix[i][j]); // ignore return value
            path[i][j] = matrix[i][j];
        }
    }

    for (int i=0; i<N; ++i)
    {
        for (int j=0; j<N; ++j)
        {
            if (i == 0 && j == 0) continue;
            else if (i == 0) path[i][j] += path[i][j-1];
            else if (j == 0) path[i][j] += path[i-1][j];
            else             path[i][j] += MIN(path[i][j-1], path[i-1][j]);

        }
    }
    printf("%d\n", path[N-1][N-1]);
}
