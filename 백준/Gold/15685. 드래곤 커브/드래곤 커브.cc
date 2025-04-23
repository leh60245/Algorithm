#include <bits/stdc++.h>
using namespace std;

using vi = vector<int>;
using vvi = vector<vector<int>>;
using pii = pair<int, int>;

int N = 101, M=101;
vvi grid(N, vi(M, 0));
vector<pii> dir_info = {{1, 0}, {0, -1}, {-1, 0}, {0, 1}};

bool oob(int i, int j)
{
    return i < 0 || N <= i || j < 0 || M <= j;
}

void draw_line(int si, int sj, vi& path)
{
    grid[si][sj] = 1;
    int ci = si, cj = sj;
    for (auto dir : path)
    {
        auto [di, dj] = dir_info[dir];
        int ni = ci + di, nj = cj + dj;
        if (oob(ni, nj)) return;
        grid[ni][nj] = 1;
        ci = ni; cj = nj;
    }
}

int count_square()
{
    int cnt = 0;
    for (int i = 0 ; i + 1 < N ; i++)
    {
        for (int j = 0 ; j + 1 < M ; j++)
        {
            if (grid[i][j] && grid[i][j+1] && grid[i+1][j] && grid[i+1][j+1]) cnt++;
        }
    }
    return cnt;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;
    for (int n = 0; n < N; n++)
    {
        int x, y, d, g;
        cin >> x >> y >> d >> g;
        vi path = {d};
        for (int t = 0 ; t < g ; t++)
        {
            int paht_lenght = path.size();
            for (int j = paht_lenght-1 ; j >= 0 ; j--)
            {
                path.push_back((path[j]+1)%4);
            }
        }
        draw_line(x, y, path);
    }
    int ans = count_square();
    cout << ans;
}
