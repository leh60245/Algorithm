#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;

template<typename T>
void print_headline(const T& s, const int& t)
{
    cout << s << t << ":\n";
}

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

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T; cin >> T;
    for (int t = 1; t <= T; t++)
    {
        print_headline("Scenario ", t);
        int N, K; cin >> N >> K; // 유저 수, 관계 수
        vi arr(N, -1);
        for (int k = 0 ; k < K ; k++)
        {
            int u, v; cin >> u >> v;
            if (u > v) swap(u, v);
            usi(u, v, arr);
        }
        int M; cin >> M; // 구할 쌍의 수
        for (int m = 0 ; m < M ; m++)
        {
            int u, v; cin >> u >> v;
            if (find(u, arr) == find(v, arr)) cout << 1 << '\n';
            else cout << 0 << '\n';
        }

        cout << '\n';
    }
}
