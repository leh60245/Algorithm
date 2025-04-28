#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;

int find(int x, vi& arr)
{
    if (arr[x] < 0)
        return x;
    return arr[x] = find(arr[x], arr);
}

bool usi(int u, int v, vi& arr)
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

int N, M; // 도시 수, 여행 계획에 속한 도시 수

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> N >> M;
    vi arr(N + 1, -1);
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            int x;
            cin >> x;
            if (x && i < j) usi(i, j, arr);
        }
    }

    int h; cin >> h;
    for (int i = 1; i < M ; i++)
    {
        int t; cin >> t;
        if (find(h, arr) != find(t, arr))
        {
            cout << "NO"; return 0;
        }
        h = t;
    }
    cout << "YES"; return 0;
}
