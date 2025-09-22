#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;
using pii = pair<int, int>;

int N;
int si, sj, siz = 2, se = 0;
vvi grid;
vector<pii> dirt = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // 상하좌우 순서

bool oob(int i, int j)
{
    return (i < 0 || i >= N || j < 0 || j >= N);
}

int mv_shark()
{
    queue<tuple<int, int, int>> q; // {row, col, distance}
    vvi visited(N, vi(N, 0));
    vector<tuple<int, int, int>> can_eat_fish; // {distance, row, col}

    q.push({si, sj, 0});
    visited[si][sj] = 1;

    while (!q.empty())
    {
        auto [ci, cj, dist] = q.front();
        q.pop();

        for (auto [di, dj] : dirt)
        {
            int ni = ci + di, nj = cj + dj;
            if (oob(ni, nj) || visited[ni][nj]) continue;
            if (grid[ni][nj] > siz) continue; // 큰 물고기는 지날 수 없음

            visited[ni][nj] = 1;
            q.push({ni, nj, dist + 1});

            // 먹을 수 있는 물고기 발견
            if (grid[ni][nj] > 0 && grid[ni][nj] < siz)
            {
                can_eat_fish.push_back({dist + 1, ni, nj});
            }
        }
    }

    if (can_eat_fish.empty()) return -1; // 먹을 수 있는 물고기 없음

    // 거리 -> 행 -> 열 순으로 정렬
    sort(can_eat_fish.begin(), can_eat_fish.end());

    auto [distance, target_i, target_j] = can_eat_fish[0];

    // 상어 이동 및 물고기 먹기
    si = target_i;
    sj = target_j;
    grid[si][sj] = 0;
    se++;

    if (se == siz)
    {
        siz++;
        se = 0;
    }

    return distance; // 이동한 거리(시간) 반환
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    grid.resize(N, vi(N, 0));

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
        {
            int v;
            cin >> v;
            if (v == 9)
            {
                si = i;
                sj = j;
                grid[i][j] = 0; // 상어 위치를 빈 칸으로 설정
            }
            else
                grid[i][j] = v;
        }

    int total_time = 0;
    while (true)
    {
        int time = mv_shark();
        if (time == -1) break; // 더 이상 먹을 물고기 없음
        total_time += time;
    }

    cout << total_time << endl;
    return 0;
}