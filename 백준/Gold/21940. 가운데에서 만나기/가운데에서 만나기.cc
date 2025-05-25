#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;
const int INF = INT_MAX / 3;

int N, M, K; // 도시 개수, 도로 개수, 인원 수
vvi cost(201, vi(201, INF));
vi city(201, 0);

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;
    for (int i = 1; i <= N; i++) cost[i][i] = 0;
    for (int m = 0; m < M; m++)
    {
        int a, b, t;
        cin >> a >> b >> t;
        cost[a][b] = t;
    }
    cin >> K;
    for (int k = 0; k < K; k++) cin >> city[k];

    for (int v = 1 ; v <= N ; v++)
        for (int i = 1 ; i <= N ; i++)
            for (int j = 1 ; j <= N ; j++)
            {
                int tmp = cost[i][v] + cost[v][j];
                if (tmp < cost[i][j])
                    cost[i][j] = tmp;
            }

    int min_cost = INT_MAX;
    vi answer;
    for (int x = 1 ; x <= N ; x++)
    {
        int tmp = 0;
        for (int k = 0 ; k < K ; k++)
        {
            int start = city[k];
            if (tmp < cost[start][x] + cost[x][start])
                tmp = cost[start][x] + cost[x][start];
        }
        if (tmp < min_cost)
        {
            min_cost = tmp;
            answer = {x};
        }
        else if (tmp == min_cost)
            answer.push_back(x);
    }
    for (auto& v : answer) cout << v << ' ';
}
