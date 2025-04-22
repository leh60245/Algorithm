#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vvc = vector<vector<char>>;
using pii = pair<int, int>;
bool DEBUG = false;

template <typename T>
void visual_grid(const vector<vector<T>>& grid, const string& name = "DEBUG")
{
    if (!DEBUG) return;
    cerr << name << ":\n";
    int N = grid.size(), M = grid[0].size();
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cout << grid[i][j] << ' ';
        }
        cout << '\n';
    }
}


int N, M;
vector<pii> blank;
vvi grid;
vvi vis;
vector<pii> dirc = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

bool oob(int i, int j)
{
    return i < 0 || N <= i || j < 0 || M <= j;
}

void bfs(int si, int sj)
{
    deque<pii> q;

    q.push_back({si, sj});
    vis[si][sj] = 1;
    while (!q.empty())
    {
        auto [ci, cj] = q.front(); q.pop_front();
        for (auto [di, dj] : dirc)
        {
            int ni = ci + di, nj = cj + dj;
            if (oob(ni, nj) || vis[ni][nj] || grid[ni][nj] == 1) continue;
            q.push_back({ni, nj});
            vis[ni][nj] = 1;
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;
    grid.resize(N, vi(M, 0));
    vis.resize(N, vi(M, 0));
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
        {
            cin >> grid[i][j];
            if (grid[i][j] == 0) blank.push_back({i, j});
        }

    vector<int> brute(blank.size(), 1);
    fill(brute.begin(), brute.end() - 3, 0);
    int ans = 0;
    do
    {
        // 벽 세우기
        for (int i = 0; i < blank.size(); i++)
            if (brute[i] == 1)
            {
                auto [bi, bj] = blank[i];
                grid[bi][bj] = 1;
            }

        // 병원 균에서 부터 시작
        int sum_blanks = 0;
        for (int i=0 ; i<N ; i++)
            for (int j=0 ; j<M ; j++)
                if (grid[i][j] == 2)
                    bfs(i, j);
        for (int i=0 ; i<N ; i++)
            for (int j=0 ; j<M ; j++)
                if (grid[i][j] == 0 && vis[i][j] == 0) sum_blanks++;
        ans = max(ans, sum_blanks);


        // 벽 허물기
        for (int i = 0; i < blank.size(); i++)
            if (brute[i] == 1)
            {
                auto [bi, bj] = blank[i];
                grid[bi][bj] = 0;
            }
        for (int i = 0; i < N; i++)
            fill(vis[i].begin(), vis[i].end(), 0);
    }
    while (next_permutation(brute.begin(), brute.end()));

    cout << ans;
}
