#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;
using tiii = tuple<int, int, int>;

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

    int N;
    cin >> N; // 논의 수
    vi arr(N + 1, -1);
    vector<tiii> edges; // i번과 j번 논을 연결하는데 드는 비용
    for (int i = 1; i <= N; i++) // 우물 파는 비용
    {
        int c;
        cin >> c;
        edges.push_back({c, 0, i});
    }
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            int c; cin >> c;
            if (i < j)
                edges.push_back({c, i, j});
        }
    }
    sort(edges.begin(), edges.end());
    int answer = 0;
    for (auto [c, n1, n2] : edges)
    {
        if (!uni(n1, n2, arr)) continue;
        answer += c;
    }
    cout << answer;
}
