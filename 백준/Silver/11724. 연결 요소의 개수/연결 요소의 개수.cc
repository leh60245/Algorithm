#include <bits/stdc++.h>
using namespace std;

int N, M;
vector<int> graph[1001];
int vis[1001];

void bfs(int start)
{
    deque<int> q;

    q.push_back(start);
    vis[start] = 1;
    while (!q.empty())
    {
        int cur = q.front(); q.pop_front();
        for (int next: graph[cur])
        {
            if (vis[next] == 1) continue;
            q.push_back(next);
            vis[next] = 1;
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N >> M;

    for (int m=0; m<M ; m++)
    {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    int ans = 0;
    for (int i=1; i<=N; i++)
    {
        if (vis[i] == 0)
        {
            bfs(i);
            ans++;
        }
    }
    cout << ans;
}
