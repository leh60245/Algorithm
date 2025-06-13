#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;
using pii = pair<int, int>;

int boundedCloud = 2;
int N, M;
vvi grid;
vector<pii> cloud;
int dx[8] = {0, -1, -1, -1, 0, 1, 1, 1};
int dy[8] = {-1, -1, 0, 1, 1, 1, 0, -1};
vector<pii> diag = {{1, 1}, {1, -1}, {-1, 1}, {-1, -1}};

bool oob(const int i, const int j) { return (i < 0 || i >= N || j < 0 || j >= N); }

void moveCloud(const int dir, const int speed)
{
    for (auto& [cx, cy] : cloud)
    {
        cx = (cx + dx[dir] * speed) % N;
        if (cx < 0)
            cx += N;
        cy = (cy + dy[dir] * speed) % N;
        if (cy < 0)
            cy += N;
    }
}

void rain()
{
    for (auto [cx, cy] : cloud)
        grid[cx][cy] += 1;
}

void magic(vector<pii>& copy_cloud)
{
    for (auto& [cx, cy] : copy_cloud)
    {
        int countBudget = 0;
        for (auto& [dx, dy] : diag)
        {
            int nx = cx + dx, ny = cy + dy;
            if (oob(nx, ny))
                continue;
            if (grid[nx][ny] > 0)
                countBudget++;
        }
        grid[cx][cy] += countBudget;
    }
}

void makeCloud(const vector<pii>& cannotMakeCloudPlace)
{
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < N; ++j)
        {
            if (find(cannotMakeCloudPlace.begin(), cannotMakeCloudPlace.end(), make_pair(i, j)) !=
                cannotMakeCloudPlace.end())
                continue;
            if (grid[i][j] >= boundedCloud)
            {
                cloud.emplace_back(i, j);
                grid[i][j] -= boundedCloud;
            }
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N >> M;
    grid.resize(N, vi(N, 0));
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
            cin >> grid[i][j];
    cloud = {{N - 1, 0}, {N - 1, 1}, {N - 2, 0}, {N - 2, 1}};


    for (int m = 1; m <= M; ++m)
    {
        int d, s; // 방향, 거리
        cin >> d >> s;
        d -= 1;
        // [1] 이동
        moveCloud(d, s);

        // [2] 비 내림
        rain();

        // [3] 구름 모두 사라짐
        auto copy_cloud = cloud;
        cloud.clear();

        // [4] [2]에서 물이 증가한 칸 물복사 버그 마법
        magic(copy_cloud);

        // [5] 구름 생성
        makeCloud(copy_cloud);
    }

    int answer = 0;
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
            answer += grid[i][j];
    cout << answer << '\n';
}
