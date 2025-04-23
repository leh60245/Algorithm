#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;
using vi = vector<int>;
using vvi = vector<vector<int>>;

int N, M;
vi graph[100001];
vi vis(100001, 0);
int need_cut = 0, need_link = 0;

void bfs(int su)
{
    deque<int> q;


    q.push_back(su);
    vis[su] = su;
    while (!q.empty())
    {
        int cu = q.front(); q.pop_front();
        for (int nu : graph[cu])
        {
            if (vis[nu] > 0)
            {
                if (nu != vis[cu])
                    need_cut++;
                continue;
            }
            q.push_back(nu);
            vis[nu] = cu;
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;
    for (int m = 0 ; m < M ; m++)
    {
        int u, v; cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    for (int u=1 ; u<=N ; u++)
    {
        if (vis[u])
            continue;
        bfs(u);
        need_link++;
    }

    int ans = 0;
    ans += need_cut / 2;
    if (need_link > 1) ans += (need_link-1);
    cout << ans;

}