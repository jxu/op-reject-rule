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
            fscanf(fp, "%d,", &matrix[i][j]); 
        }
    }

    for (int i=0; i<N; ++i)
        path[i][0] = matrix[i][0];

    for (int j=1; j<N; ++j)
    {
        for (int i1=0; i1<N; ++i1)
        {
            int min_col_path = 1e9;
            for (int i0=0; i0<N; ++i0) 
            {
                int col_path = path[i0][j-1];
                for (int i2=MIN(i0,i1); i2<=MAX(i0,i1); ++i2)
                    col_path += matrix[i2][j];

                min_col_path = MIN(min_col_path, col_path);
            }
            path[i1][j] = min_col_path;
        }
    }

    int res = 1e9;
    for (int i=0; i<N; ++i)
        res = MIN(res, path[i][N-1]);

    printf("%d\n", res);

}
