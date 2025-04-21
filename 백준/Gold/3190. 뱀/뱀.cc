#include <bits/stdc++.h>
using namespace std;
bool DEBUG = false;

/* 뱀이 사과 먹으면 길이(size++), 벽 또는 자신 몸 부딪히면 게임 끝
 * 게임은 NxN 정사각형 보드 위, 상하좌우 끝에 벽 있음,
 * 게임 시작 시 뱀은 맨위좌측에 위치, 뱀 길이는 1, 처음에 오른쪽으로 향함
 * [뱀 이동 규칙]
 * 1. 뱀은 몸 길이 늘려 머리 다음 칸에 위치
 *      다음칸을 확인해야 한다.
 * 2. [종료 조건] 벽, 몸에 부딛히면 게임 끝
 * 3. 이동한 칸에 사과 있으면
 *      -> (1) 그 칸 사과 없어지고, (2) 꼬리 움직이지 않음
 * 4. 이동한 칸에 사과 없으면
 *      -> 몸 길이 줄여 꼬리 위치 칸 비움 (몸 길이 그대로)
 *
 * [목표] 게임이 몇 초에 끝나는지 계산하라.
 *
 * [조건]
 * 시작 시간으로 부터 x초가 끝난 뒤 90도 방향 회전. L = 왼쪽, D = 오른쪽
 */
int N, K, L; //
vector<vector<int>> grid; // 사과=1
deque<pair<int, int>> body; // { 머리, ... , 꼬리 }
int di[] = {0, 1, 0, -1};
int dj[] = {1, 0, -1, 0};

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N >> K;
    grid.resize(N, vector<int>(N, 0));
    for (int k = 0; k < K; k++)
    {
        int x, y;
        cin >> x >> y;
        x--;
        y--;
        grid[x][y] = 1;
    }
    cin >> L;
    int dir = 0, time = 0;
    body.push_back({0, 0});
    for (int l = 0; l < L+1; l++)
    {
        int ntime;
        char cmd;
        if (l < L) cin >> ntime >> cmd;
        else ntime = time + N;
        // time 만큼 이동
        int ni, nj;
        while (time < ntime)
        {
            time++;
            auto [ci, cj] = body.front(); // 머리 정보만 가져옴.
            ni = ci + di[dir];
            nj = cj + dj[dir]; // 머리의 다음 위치 정보
            if (ni < 0 || N <= ni || nj < 0 || N <= nj
                || find(body.begin(), body.end(), make_pair(ni, nj)) != body.end())
            {
                cout << time;
                return 0;
            }
            body.push_front({ni, nj});
            if (grid[ni][nj]) grid[ni][nj] = 0;
            else body.pop_back();
        }
        // cout << "time: " << time << " body size: " << body.size() << " head is " << body.front().first << ' ' << body.front().second << '\n';
        // 방향 바꾸기
        if (cmd == 'L') dir = (dir + 3) % 4;
        else dir = (dir + 1) % 4;
    }
    cout << time;
}
