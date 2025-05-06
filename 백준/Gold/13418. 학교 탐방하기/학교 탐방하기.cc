#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;
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
    int N, M;
    cin >> N >> M;
    vi arr(N + 1, -1);
    vector<tiii> edges;
    for (int m = 0; m <= M; m++)
    {
        int n1, n2, c;
        cin >> n1 >> n2 >> c;
        edges.emplace_back(1- c, n1, n2);
    }
    sort(edges.begin(), edges.end());
    int min_cost = 0;
    for (auto& [c, n1, n2] : edges)
    {
        if (!uni(n1, n2, arr)) continue;
        min_cost += c;
    }
    min_cost *= min_cost;
    fill(arr.begin(), arr.end(), -1);

    sort(edges.begin(), edges.end(), [](const auto& a, const auto& b)
    {
        return get<0>(a) > get<0>(b);
    });
    int max_cost = 0;
    for (auto& [c, n1, n2] : edges)
    {
        if (!uni(n1, n2, arr)) continue;
        max_cost += c;
    }
    max_cost *= max_cost;

    cout << max_cost - min_cost;
}
