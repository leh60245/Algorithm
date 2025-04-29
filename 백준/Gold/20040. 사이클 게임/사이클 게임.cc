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

int N, M; 

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> N >> M;
    vi arr(N, -1);
    for (int m = 1 ; m <= M ; m++)
    {
        int x, y; cin >> x >> y;
        if (!usi(x, y, arr))
        {
            cout << m;
            return 0;
        };

    }
    cout << 0;
}
