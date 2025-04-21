#include <bits/stdc++.h>
using namespace std;

int N=12, M=6;
vector<vector<char>> grid(N, vector<char>(M));
vector<vector<int>> vis(N, vector<int>(M, 0));
vector<pair<int, int>> dij = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

template<typename T>
void printGrid(const vector<vector<T>>& g , const string& name = "grid") {
    cerr << name <<'\n';
    for (auto& row : g) {
        for (auto& val : row)
            cerr << val << ' ';
        cerr << '\n';
    }
    cerr << '\n';
}

int bfs(int si, int sj)
{
    deque<pair<int,int>> q;
    vector<pair<int, int>> path;
    int cnt = 0;
    char color = grid[si][sj];

    q.push_back({si, sj});
    path.push_back({si, sj});
    vis[si][sj] = 1;
    cnt++;
    while (!q.empty())
    {
        auto [ci, cj] = q.front(); q.pop_front();
        for (auto [di, dj] : dij)
        {
            int ni = ci + di, nj = cj + dj;
            if (ni < 0 || N <= ni || nj < 0 || M <= nj || vis[ni][nj] == 1 || grid[ni][nj] != color) continue;
            q.push_back({ni ,nj});
            path.push_back({ni, nj});
            vis[ni][nj] = 1;
            cnt++;
        }
    }
    if (cnt >= 4)
    {
        for (auto [i, j]: path) grid[i][j] = '.';
        return 1;
    }
    return 0;
}

void gravity() {
    for (int j = 0; j < M; j++) {
        vector<char> col;
        for (int i = N - 1; i >= 0; i--) {
            if (grid[i][j] != '.') col.push_back(grid[i][j]);
        }
        int idx = N - 1;
        for (char val : col) grid[idx--][j] = val;
        while (idx >= 0) grid[idx--][j] = '.';
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    for (int i=0 ; i<N ; i++)
        for (int j=0; j<M ; j++)
            cin >> grid[i][j];

    int ans=0;
    int t = 1;
    while (true)
    {
        // cerr << "============== " << t << " ===============\n";
        for (int i = 0; i < N; i++)
            fill(vis[i].begin(), vis[i].end(), 0);
        // 터트리기
        int boom = 0;
        for (int i=0; i<N ; i++)
            for (int j=0; j<M ; j++)
                if (grid[i][j] != '.' && vis[i][j] != 1)
                {
                    boom += bfs(i, j);
                }
        // printGrid(grid, "after boom");
        // 터지는게 없으면 종료
        if (!boom) break;
        ans++;
        // 중력
        gravity();
        // printGrid(grid, "after gravity");
        t++;

    }
    cout << ans;
    return 0;
}