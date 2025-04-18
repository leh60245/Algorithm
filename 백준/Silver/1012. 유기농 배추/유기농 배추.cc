#include <bits/stdc++.h>
using namespace std;

/* 한 배추에 배추 흰지렁이가 한 마리라도 살고 있다면 -> 이 지렁이는 인접한 다른 배추로 이동 가능
 * 인접: 상하좌우
 *
 * 배추들이 모여있는 곳에는 지렁이 한 마리만 있으면 됨.
 * 따라서 서로 인접한 배추들이 몇 군데 퍼져있는지 조사하면 총 마리수 구할 수 있음
 * [목표] 최소 지렁이 마리 수 출력
 */
int T, N, M, K;
int grid[52][52];
int vis[52][52];
int di[4] = {0, 1, 0, -1};
int dj[4] = {1, 0, -1, 0};

void bfs(int si, int sj)
{
    deque<pair<int, int>> q;

    q.push_back({si, sj});
    vis[si][sj] = 1;
    while (!q.empty())
    {
        auto [ci, cj] = q.front(); q.pop_front();
        for (int dir=0; dir<4; dir++)
        {
            int ni = ci + di[dir];
            int nj = cj + dj[dir];
            if (ni < 0 || N <= ni || nj < 0 || M <= nj || vis[ni][nj] == 1 || grid[ni][nj] == 0) continue;
            q.push_back({ni ,nj});
            vis[ni][nj] = 1;
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> T;
    while (T--)
    {
        int ans=0;
        cin >> M >> N >> K;
        for (int k=0; k<K ; k++)
        {
            int i, j;
            cin >> j >> i;
            grid[i][j] = 1;
        }
        for (int i=0; i<N ; i++)
            for (int j=0; j<M ; j++)
                if (grid[i][j] == 1 && vis[i][j] == 0)
                {
                    bfs(i ,j);
                    ans++;
                }
        cout << ans << '\n';
        memset(grid, 0, sizeof(grid));
        memset(vis, 0, sizeof(vis));
    }

}
