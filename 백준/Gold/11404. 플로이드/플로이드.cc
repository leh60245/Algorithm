#include <bits/stdc++.h>
#define MAX_COST 0x3f3f3f3f
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;
using tiii = tuple<int, int, int>;

int find(int x, vi& arr)
{
    if (arr[x] < 0)
        return x;
    return arr[x] = find(arr[x], arr);
}

bool uni(int u, int v, vi& arr)
{
    u = find(u, arr);
    v = find(v, arr);
    if (u == v)
        return false;
    if (arr[v] < arr[u])
        swap(u, v);
    if (arr[u] == arr[v])
        arr[u]--;
    arr[v] = u;
    return true;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    vvi grid(N + 1, vi(N + 1, MAX_COST));
    for (int i = 1; i <= N; i++) grid[i][i] = 0;
    for (int m = 0; m < M; m++)
    {
        int i, j, c;
        cin >> i >> j >> c;
        grid[i][j] = min(grid[i][j], c);
    }
    for (int v = 1; v <= N; v++)
    {
        for (int i = 1; i <= N; i++)
        {
            for (int j = 1; j <= N; j++)
            {
                // if (v == i || v == j || i == j) continue;
                grid[i][j] = min(grid[i][j], grid[i][v] + grid[v][j]);
            }
        }
    }
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            if (grid[i][j] == MAX_COST)
            {
                cout << 0 << ' ';
            }
            else
            {
                cout << grid[i][j] << ' ';
            }
        }
        cout << '\n';
    }
}
