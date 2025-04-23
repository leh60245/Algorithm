#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;
using vi = vector<int>;
using vvi = vector<vector<int>>;


int N, M;
vvi graph(1001, vi(1001, 0));

int bfs(int si, int ei)
{
    deque<int> q;
    vi vis(1001, 0);

    q.push_back(si);
    vis[si] = 1;
    while (!q.empty())
    {
        int ci = q.front(); q.pop_front();
        if (ci == ei) return vis[ei] - 1;
        for (int ni = 1 ; ni <= N ; ni++)
        {
            if (ci == ni || graph[ci][ni] == 0 || vis[ni] > 0) continue;
            q.push_back(ni);
            vis[ni] = vis[ci] + graph[ci][ni];
        }
    }
    return -1;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;
    for (int i=0 ; i<N-1 ; i++)
    {
        int u, v, l; cin >> u >> v >> l;
        graph[u][v] = l;
        graph[v][u] = l;
    }

    for (int m=0 ; m < M ; m++)
    {
        int u, v; cin >> u >> v;
        cout << bfs(u, v) << '\n';
    }

}