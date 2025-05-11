#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    const int INF = INT_MAX / 3;
    vvi grid(N + 1, vi(N + 1, INF));
    vvi nxt(N + 1, vi(N + 1, 0));
    for (int i = 1; i <= N; i++)
        grid[i][i] = 0;

    for (int m = 0; m < M; m++)
    {
        int n1, n2, cost;
        cin >> n1 >> n2 >> cost;
        grid[n1][n2] = min(grid[n1][n2], cost); // 문제에서 중복은 없다고 함
        nxt[n1][n2] = n2;
    }

    for (int v = 1; v <= N; v++)
        for (int i = 1; i <= N; i++)
            for (int j = 1; j <= N; j++)
            {
                if (v == i || i == j || v == j) continue;
                if (grid[i][j] > grid[i][v] + grid[v][j])
                {
                    grid[i][j] = grid[i][v] + grid[v][j];
                    nxt[i][j] = nxt[i][v];
                }
            }

    // 비용 그리기
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            if (grid[i][j] == INF) cout << 0 << ' ';
            else cout << grid[i][j] << ' ';
        }
        cout << '\n';
    }

    // 경로 복원하기
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            if (grid[i][j] == 0 || grid[i][j] == INF)
            {
                cout << 0 << '\n';
                continue;
            }
            vi path;
            int start = i;
            while (start != j)
            {
                path.push_back(start);
                start = nxt[start][j];
            }
            path.push_back(j);

            cout << path.size() << ' ';
            for (auto& v : path) cout << v << ' ';
            cout << '\n';
        }
    }
}
