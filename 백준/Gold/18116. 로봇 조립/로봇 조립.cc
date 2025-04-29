#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;

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
    vi arr(1000001, -1);
    vi par(1000001, 1);
    for (int n = 1; n <= N; n++)
    {
        char cmd;
        cin >> cmd;
        if (cmd == 'I')
        {
            int x, y;
            cin >> x >> y;
            if (x > y) swap(x, y);
            int x_head = find(x, arr);
            int y_head = find(y, arr);
            int x_parts = par[x_head];
            int y_parts = par[y_head];
            if (uni(x, y, arr))
            {
                if (find(x, arr) == x_head)
                    par[x_head] += y_parts;
                else
                    par[y_head] += x_parts;
            }

        }
        else
        {
            int x;
            cin >> x;
            int cnt = par[find(x, arr)];
            cout << cnt << '\n';
        }
    }
}
