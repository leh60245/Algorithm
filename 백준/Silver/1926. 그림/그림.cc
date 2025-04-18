#include <bits/stdc++.h>
using namespace std;

/* [목표] 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력
 * 단, 그림은 1로 연결, 넓이는 그림에 포함된 1의 개수
 */
bool DEBUG = false;
int N, M;
int grid[502][502];
int vis[502][502];
int di[4] = {1, 0, -1, 0};
int dj[4] = {0, 1, 0, -1};

int bfs(int si, int sj)
{
    int cnt =0;
    deque<pair<int,int>> q;

    q.push_back({si, sj});
    vis[si][sj] = 1;

    while (!q.empty())
    {
        auto [ci, cj] = q.front(); q.pop_front();
        ++cnt;

        for (int dir=0; dir<4; dir++)
        {
            int ni = ci + di[dir];
            int nj = cj + dj[dir];
            if (ni < 0 || N <= ni || nj < 0 || M <= nj || vis[ni][nj] == 1) continue;
            if (grid[ni][nj] == 1)
            {
                q.push_back({ni, nj});
                vis[ni][nj] = 1;
            }
        }
    }

    return cnt;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;
    for (int i=0; i<N; i++)
        for (int j=0; j<M; j++)
            cin >> grid[i][j];

    int cnt_pic = 0;
    int max_size = 0;
    for (int i=0; i<N; i++)
        for (int j=0; j<M; j++)
            if (grid[i][j] == 1 && vis[i][j] == 0)
            {
                if (DEBUG) cout << i << ' ' << j << '\n';
                cnt_pic++;
                int tmp = bfs(i, j);
                if (tmp > max_size) max_size = tmp;
            }
    cout << cnt_pic << '\n' << max_size;
}
