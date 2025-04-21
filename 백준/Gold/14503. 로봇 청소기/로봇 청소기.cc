#include <bits/stdc++.h>
// #include "debug_utils.h"
using namespace std;

#ifdef LOCAL
#define DEBUG_MODE true
#else
#define DEBUG_MODE false
#endif
bool DEBUG = DEBUG_MODE;


/* NxM 직사각형, 빈칸=0, 벽=1
 * 가장 왼위 0,0
 * [작동 방식]
 * 1. 지금 칸 청소 x -> 지금 칸 청소
 * 2. 지금 칸 주변 4칸이
 *      1) 모두 청소 되어 있다면,
 *          바라보는 방향 유지한 채, 한 칸 후진 후 1번으로
 *          만약 뒤쪽 칸이 벽이라 후진할 수 없으면 작동 멈춤
 *      2) 청소되지 않은 빈 칸이 있다면,
 *          반시계 방향으로 90도 회전. (dir--)
 *          바라보는 방향 기준으로 앞쪽 칸이 청소되지 않은 빈칸이라면, 한 칸 전진
 *          1번으로 돌아감
 *
 * [목표] 작동 멈출 때 까지 청소하는 칸의 개수 출력
 */
int N, M;
int ci, cj, dir;
int di[] = {-1, 0, 1, 0};
int dj[] = {0, 1, 0, -1};

vector<vector<int>> grid;
vector<vector<int>> vis;



int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N >> M;
    cin >> ci >> cj >> dir;
    grid.resize(N, vector<int>(M, 0));
    vis.resize(N, vector<int>(M, 0));
    for (int i=0 ; i<N ; i++)
        for (int j=0; j<M ; j++)
            cin >> grid[i][j];

    vis[ci][cj] = 1;
    int ans = 1;
    while (true)
    {
        bool can_clean = false;
        int ni = ci, nj = cj, n_dir = dir;
        for (int d=1; d<5 ; d++)
        {
            n_dir = (dir - d + 4) % 4;
            ni = ci + di[n_dir];
            nj = cj + dj[n_dir];
            if (vis[ni][nj]) continue;
            if (grid[ni][nj]) continue;
            can_clean = true;
            vis[ni][nj] = 1;
            ans++;
            break;
        }
        if (can_clean)
        {
            ci = ni; cj = nj; dir = n_dir;
            continue;
        }
        n_dir = (dir + 2) % 4;
        ni = ci + di[n_dir];
        nj = cj + dj[n_dir];
        if (grid[ni][nj])
        {
            cout << ans;
            return 0;
        }
        ci = ni; cj = nj;
    }
    cout << ans;
    return 0;
}
