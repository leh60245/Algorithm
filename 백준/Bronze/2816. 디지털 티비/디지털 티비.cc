#include <bits/stdc++.h>
#define K1 "KBS1"
#define K2 "KBS2"
using namespace std;
using vi = vector<int>;
using vs = vector<string>;


int N;
vi cmd;
vs grid;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    grid.resize(N, "");
    for (int i = 0; i < N; i++) cin >> grid[i];
    int p = 0;
    if (grid[p] == K1)
    {
    }
    else if (grid[p + 1] == K1)
    {
        swap(grid[p], grid[p + 1]);
        cmd.push_back(3);
        p++;
    }
    else
    {
        while (grid[p] != K1)
        {
            cmd.push_back(1);
            p++;
        }
        while (p > 0)
        {
            swap(grid[p], grid[p - 1]);
            cmd.push_back(4);
            p--;
        }
    }

    if (p == 0 && grid[p + 1] == K2)
    {
    }
    else if (p == 1 && grid[p + 1] == K2)
    {
        swap(grid[p], grid[p + 1]);
        cmd.push_back(3);
        p++;
    }
    else
    {
        while (grid[p] != K2)
        {
            cmd.push_back(1);
            p++;
        }
        while (p > 1)
        {
            swap(grid[p], grid[p - 1]);
            cmd.push_back(4);
            p--;
        }
    }


    for (const int& v : cmd) cout << v;
    return 0;
}
