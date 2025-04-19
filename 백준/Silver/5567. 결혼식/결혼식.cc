#include <bits/stdc++.h>
using namespace std;

int N, M;
vector<int> graph[502];
int vis[502];

int bfs(int start)
{
    deque<int> q;
    int path = 0;

    q.push_back(start);
    vis[start] = 1;
    while (!q.empty())
    {
        int cur = q.front(); q.pop_front();
        if (vis[cur] > 2) continue;
        for (int next: graph[cur])
        {
            if (vis[next] >= 1) continue;
            q.push_back(next);
            vis[next] = vis[cur] + 1;
            path++;
        }
    }

    return path;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;
    for (int m=0 ; m<M ; m++)
    {
        int x, y;
        cin >> x >> y;
        graph[x].push_back(y);
        graph[y].push_back(x);
    }

    int ans = bfs(1);
    cout << ans;
}
