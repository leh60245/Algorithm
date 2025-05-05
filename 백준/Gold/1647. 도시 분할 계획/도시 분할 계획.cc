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

/* N개 집과 M개 길. 길은 어느 방향으로도 다닐 수 있음
 * 길 마다 유지비 있고, 임의의 두 집 사이 경로 항상 존재
 * 마을 2개로 분리. 분리할 때 각 분리 마을 안에 집 서로 연결되도록 분할
 * 각 분리 마을 안에 임의의 두 집 사이 경로 항상 존재
 * 마을에는 집 하나 이상
 *
 * 분리된 두 마을간 길들 삭제
 * 유지비 최소로 다른 길 삭제
 */

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M ; cin >> N >> M;
    vi arr(N+1, -1);
    vector<tiii> costs;
    for (int m=0 ; m<M ; m++)
    {
        int n1, n2, cost; cin >> n1 >> n2 >> cost;
        costs.emplace_back(cost, n1, n2);
    }
    sort(costs.begin(), costs.end());
    int total_cost = 0;
    int max_cost = 0;
    for (auto& [c, n1, n2] : costs)
    {
        if (!uni(n1, n2, arr)) continue;
        total_cost += c;
        max_cost = max(max_cost, c);
    }
    cout << total_cost - max_cost;
}
