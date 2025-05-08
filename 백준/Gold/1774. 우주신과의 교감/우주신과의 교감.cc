#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;
using pii = pair<int, int>;
using tiii = tuple<int, int, int>;
using ll = long long;

int find(int x, vi& arr)
{
    if (arr[x] < 0)
        return x;
    return arr[x] = find(arr[x], arr);
}

bool uni(int u, int v, vi& arr)
{
    u = find(u, arr);
    v = find(v, arr);
    if (u == v)
        return false;
    if (arr[v] < arr[u])
        swap(u, v);
    if (arr[u] == arr[v])
        arr[u]--;
    arr[v] = u;
    return true;
}


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M; cin >> N >> M;
    vi arr(N+1, -1);
    vector<pii> nodes;
    vector<tuple<double, int, int>> costs;
    for (int n=0 ; n < N ; n++)
    {
        int x, y; cin >> x >> y;
        nodes.emplace_back(x, y);
    }
    for (int i = 0 ; i < N-1 ; i++)
    {
        for (int j = i+1; j < N ; j++)
        {
            auto& [x1, y1] = nodes[i];
            auto& [x2, y2] = nodes[j];
            double cost = sqrt(pow(x1-x2, 2) + pow(y1-y2, 2));
            costs.emplace_back(cost, i+1, j+1);
        }
    }
    for (int m=0 ; m < M ; m++)
    {
        int n1, n2; cin >> n1 >> n2;
        uni(n1, n2, arr);
    }
    sort(costs.begin(), costs.end());
    double answer = 0;
    for (auto& [c, n1, n2] : costs)
    {
        if (!uni(n1, n2, arr)) continue;
        answer += c;
    }
    cout << fixed << setprecision(2) << answer << '\n';
}
