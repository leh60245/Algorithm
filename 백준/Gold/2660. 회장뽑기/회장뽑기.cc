#include <bits/stdc++.h>
using namespace std;

int N;
vector<int> graph[52];
int vis[52];

int bfs(int start)
{
    deque<int> q;

    q.push_back(start);
    vis[start] = 1;
    while (!q.empty())
    {
        int cur = q.front(); q.pop_front();

        for (int next: graph[cur])
        {
            if (vis[next] >= 1) continue;
            q.push_back(next);
            vis[next] = vis[cur] + 1;
        }
    }

    int mx=0;
    for (int i=1; i<=N; ++i)
    {
        mx = max(mx, vis[i]);
    }
    return mx - 1 ;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N ;
    while (true)
    {
        int x, y;
        cin >> x >> y;
        if (x==-1) break;
        graph[x].push_back(y);
        graph[y].push_back(x);
    }
    vector<int> ans_idx;
    int ans_min=60;
    for (int n=1; n<=N ; n++)
    {
        memset(vis, 0, sizeof(vis));
        int tmp = bfs(n);
        if (tmp == 0) continue;
        if (tmp == ans_min)
        {
            ans_idx.push_back(n);
        }
        else if (tmp < ans_min)
        {
            ans_idx.clear();
            ans_idx.push_back(n);
            ans_min = tmp;
        }
    }
    cout << ans_min << ' ' << ans_idx.size() <<'\n';
    for (int v : ans_idx) cout << v << ' ';

}
