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

    int T;
    cin >> T;
    while (T--)
    {
        int N, M;
        cin >> N >> M;
        vi arr(N + 1, -1);
        vector<tiii> cost;
        for (int m = 0; m < M; m++)
        {
            int n1, n2;
            cin >> n1 >> n2;
            cost.push_back({1, n1, n2});
        }
        int answer = 0;
        sort(cost.begin(), cost.end());
        for (auto& [c, n1, n2] : cost)
        {
            if (!uni(n1, n2, arr)) continue;
            answer += c;
        }
        cout << answer << '\n';
    }
}
