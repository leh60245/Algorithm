#include <bits/stdc++.h>
using namespace std;
using path = vector<pair<int, int>>;
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

/* [폴리오미노 조건]
 * 1. 정사각형 겹치지 않기
 * 2. 모두 연결 (상하좌우)
 * 3. 변끼리 연결.
 *  -> 5가지
 *  => '회전'이나 '대칭' 가능 -> 5*? 가지 있음
 * NxM 종이 위 테트로미노 하나 놓음. 각 칸에 정수 하나 쓰여짐
 * 테트로미노 하나 적절히 놓음
 *
 * [목표] 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로
 */
int N, M;
vector<vector<int>> grid;
vector<vector<int>> vis;
vector<pair<int, int>> dist = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
int ans = 0;

bool oob(int i, int j)
{
    return i < 0 || N <= i || j < 0 || M <= j;
}

vector<vector<int>> tmp_vis;
void dfs(int si, int sj, int depth, int sum_v)
{
    if (depth == 4)
    {
        ans = max(ans, sum_v);
        return;
    }
    for (auto [di, dj] : dist)
    {
        int ni = si + di, nj = sj + dj;
        if (oob(ni ,nj) || vis[ni][nj] || tmp_vis[ni][nj]) continue;
        tmp_vis[ni][nj] = 1;
        dfs(ni, nj, depth+1, sum_v + grid[ni][nj]);
        if (depth == 2)
            dfs(si, sj, depth+1, sum_v + grid[ni][nj]);
        tmp_vis[ni][nj] = 0;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;
    grid.resize(N, vector<int>(M, 0));
    vis.resize(N, vector<int>(M, 0));
    tmp_vis.resize(N, vector<int>(M, 0));
    for (int i=0; i<N; i++)
        for (int j=0; j<M ; j++)
            cin >> grid[i][j];

    for (int i=0; i<N; i++)
    {
        for (int j=0; j<M; j++)
        {
            tmp_vis[i][j] = 1;
            dfs(i, j, 1, grid[i][j]);
            tmp_vis[i][j] = 0;
        }
        for (int j=0; j<M; j++)
            vis[i][j] = 1;
    }
    cout << ans;
}
