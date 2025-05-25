#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;
const int INF = INT_MAX / 3;


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int N, M, R;
    cin >> N >> M >> R;
    vi item(N + 1, 0);
    vvi dist(N + 1, vi(N + 1, INF));


    for (int i = 1; i <= N; i++)
        cin >> item[i];
    for (int i = 1; i <= N; ++i)
        dist[i][i] = 0;

    for (int r = 0; r < R; r++)
    {
        int a, b, l;
        cin >> a >> b >> l;
        dist[a][b] = l;
        dist[b][a] = l;
    }

    for (int v = 1; v <= N; v++)
        for (int i = 1; i <= N; i++)
            for (int j = 1; j <= N; j++)
            {
                int tmp = dist[i][v] + dist[v][j];
                if (tmp < dist[i][j])
                    dist[i][j] = tmp;
            }

    int ans = 0;
    for (int i = 1; i <= N; i++)
    {
        int tmp = 0;
        for (int j = 1; j <= N; j++)
        {
            if (dist[i][j] <= M)
                tmp += item[j];
        }
        ans = max(ans, tmp);
    }
    cout << ans;
}
