#include <bits/stdc++.h>
using namespace std;

int K;
int V, E; // 그래프 정점 개수, 간선 개수
vector<int> graph[20001];
int vis[20001];


bool bfs()
{
    for (int si=1; si<=V; si++)
    {
        if (vis[si] >= 1) continue;
        deque<int> q;

        q.push_back(si);
        vis[si] = 1;
        while (!q.empty())
        {
            int ci = q.front(); q.pop_front();

            for (int ni:graph[ci])
            {
                if (vis[ni] >= 1)
                {
                    if (vis[ci] == vis[ni]) return false;
                    continue;
                }
                q.push_back(ni);
                vis[ni] = 3 - vis[ci];
            }
        }
    }
    return true;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> K;   // 테스트 케이스 개수
    while (K--)
    {
        cin >> V >> E;
        for (int e=0; e<E ; e++)
        {
            int u, v;
            cin >> u >> v;
            graph[u].push_back(v);
            graph[v].push_back(u);
        }
        bool ans = bfs();
        if (ans) cout << "YES" << '\n';
        else cout << "NO" << '\n';

        memset(graph, 0, sizeof(graph));
        memset(vis, 0, sizeof(vis));
    }

}
