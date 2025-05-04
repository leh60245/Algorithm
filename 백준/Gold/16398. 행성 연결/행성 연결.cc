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

    int N;
    cin >> N;
    vi arr(N+1, -1);
    vector<tiii> costs;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
        {
            int x;
            cin >> x;
            if (i < j) costs.emplace_back(x, i+1, j+1);
        }
    sort(costs.begin(), costs.end());

    ll answer = 0;
    for (auto& [c, n1, n2] : costs)
    {
        if (!uni(n1, n2, arr)) continue;
        answer += c;
    }
    cout << answer;
}
