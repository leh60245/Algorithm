#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vector<int>>;
bool DEBUG = false;


template<typename T>
void visual_grid(const vector<vector<T>>& grid, const string& name = "DEBUG")
{
    if (!DEBUG) return;
    cerr << name << ":\n";
    int N = grid.size(), M=grid[0].size();
    for (int i=0; i<N ; i++)
    {
        for (int j=0; j<M ; j++)
        {
            cout << grid[i][j] << ' ';
        }
        cout << '\n';
    }
}


int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N ; cin >> N;
    while (N > 1)
    {
        bool is_find = false;
        for (int i = 2 ; i <= N ; i++)
        {
            if (N % i == 0)
            {
                is_find = true;
                N = N / i;
                cout << i << '\n';
                break;
            }
        }
        if (is_find) continue;
        break;
    }


}
