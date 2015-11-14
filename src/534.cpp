#include <iostream>
#include <vector>


using namespace std;

const int n = 4;
long long counter = 0;


void Q(vector<int> &board, int l, int w)
{
    if (l == n)
    {
        counter++;
        //for (auto x : board)
        //    cout << x << ' ';
        //cout << endl;
        return;
    }

    for (int x=0; x<n; x++)
    {
        bool valid = true;
        for (int j=max(l-n+1+w, 0); j<l; j++)
        {
            if (x == board[j] or l-j == abs(x - board[j]))
            {
                valid = false;
                break;
            }
        }

        if (valid)
        {
            board[l] = x;
            Q(board, l+1, w);
        }
    }

}

int main()
{
    for (int w=0; w<=n-1; w++)
    {

        for (int start=0; start<n/2; start++) // Symmetry
        {
            vector<int> board(n);
            board[0] = start;
            Q(board, 1, w);

        }
    }



    cout << 2*counter << endl;
    return 0;
}
