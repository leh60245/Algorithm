#include <bits/stdc++.h>
using namespace std;

int N;
vector<int> graph[100001];
int parent[100001];

void bfs(int si)
{
    fill(parent , parent+N+1, -1);
    deque<int> q;

    q.push_back(si);
    parent[si] = 0;
    while (!q.empty())
    {
        int cur = q.front(); q.pop_front();
        for (int nxt: graph[cur])
        {
            if (parent[nxt] != -1) continue;
            parent[nxt] = cur;
            q.push_back(nxt);
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    for (int p=1; p<=N-1; p++)
    {
        int u, v; cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    bfs(1);
    for (int p=2; p<=N; p++) cout << parent[p] << '\n';
}



