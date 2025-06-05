#include <bits/stdc++.h>
using namespace std;
using vc = vector<char>;
using vvc = vector<vc>;
using vi = vector<int>;
using vvi = vector<vi>;
using pii = pair<int, int>;

int N, M, T;
vvc grid;
vvi v;
vector<pii> dirt = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

void visual_grid()
{
    for (int i = 0 ; i < N ; i++)
    {
        for (int j = 0 ; j < M ; j++)
            cout << grid[i][j];
        cout << '\n';
    }
}

bool oob(const int i, const int j)
{
    return (i < 0 || i >= N || j < 0 || j >= M);
}

bool broke_block(const int i, int j)
{
    const int tmp = j == 0 ? 1 : -1;
    const int end_j = M - j - 1;
    while (j != end_j)
    {
        if (grid[i][j] == 'x')
        {
            grid[i][j] == '.';
            return true;
        }
        j += tmp;
    }
    return false;
}

void bfs(const int si, const int sj, const int gn)
{
    deque<pair<int, int>> q;

    q.emplace_back(si, sj);
    v[si][sj] = gn;
    while (!q.empty())
    {
        auto [ci, cj] = q.front();
        q.pop_front();
        for (auto [di, dj] : dirt)
        {
            const int ni = ci + di, nj = cj + dj;
            if (oob(ni ,nj)) continue;
            if (grid[ni][nj] == '.' || v[ni][nj]) continue;
            q.emplace_back(ni ,nj);
            v[ni][nj] = gn;
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while (true)
    {
        int x, y;
        cin >> x >> y;
        if (x == 0 && y == 0) break;
        if (x > y) cout << "Yes\n";
        else cout << "No\n";
    }

}
