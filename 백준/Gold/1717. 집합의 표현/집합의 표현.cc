#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;

int N, M;
vi arr;


int find(int x)
{
    if (arr[x] < 0)
        return x;
    return arr[x] = find(arr[x]);
}

bool usi(int u, int v)
{
    u = find(u);
    v = find(v);
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

    cin >> N >> M;
    arr.resize(N + 1, -1);
    for (int m = 0; m < M; m++)
    {
        int cmd, a, b;
        cin >> cmd >> a >> b;
        if (cmd == 0) // 합집합 연산
        {
            usi(a, b);
        }
        else // 찾기 연산
        {
            if (find(a) == find(b)) cout << "YES" << '\n';
            else cout << "NO" << '\n';
        }
    }
}
