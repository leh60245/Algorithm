#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;

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

vi arr;
vector<tuple<int, int, int>> edges;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int V, E; cin >> V >> E;
    arr.resize(V+1, -1);
    for (int e=0; e < E ; e++)
    {
        int n1, n2, c; cin >> n1 >> n2 >> c;
        edges.push_back({c, n1, n2});
    }
    sort(edges.begin(), edges.end());
    int cost = 0;
    for (int i = 0 ; i < E; i++)
    {
        int c, n1, n2;
        tie(c, n1, n2) = edges[i];
        if (!uni(n1, n2, arr)) continue;
        cost += c;
    }
    cout << cost;


}
