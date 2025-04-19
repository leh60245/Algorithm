#include <bits/stdc++.h>
using namespace std;

int N, M;
vector<int> graph[501];
bool vis[501];

pair<int,int> bfs(int si)
{
    deque<int> q;

    q.push_back(si);
    vis[si] = true;
    int num_node = 1, num_edge = 0;
    while (!q.empty())
    {
        int cur = q.front(); q.pop_front();
        for (int nxt: graph[cur])
        {
            num_edge++;
            if (vis[nxt]) continue;
            q.push_back(nxt);
            vis[nxt] = true;
            num_node++;
        }
    }

    num_edge /= 2;
    return {num_node, num_edge};
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t = 0;
    while (t++>=0)
    {
        cin >> N >> M;
        if (N==0 && M==0) break;

        for (int i=0; i<=N; ++i)
            graph[i].clear();
        fill(vis, vis+N+1, false);

        while (M--)
        {
            int u, v; cin >> u >> v;
            graph[u].push_back(v);
            graph[v].push_back(u);
        }
        int cnt = 0;
        for (int n=1; n<=N; n++)
            if (vis[n] == 0)
            {
                auto [num_node, num_edge] = bfs(n);
                if (num_node == num_edge+1) cnt++;
            }

        cout << "Case " << t << ": ";
        if (cnt == 0) cout << "No trees." ;
        else if (cnt == 1) cout << "There is one tree.";
        else cout << "A forest of " << cnt << " trees.";
        cout << '\n';
    }

}



