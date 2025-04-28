#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;


int N, M;
vvi graph;
vi indegree;
vi answer;


void bfs()
{
    deque<int> q;

    for (int i = 1 ; i <= N ; i++)
    {
        if (indegree[i] == 0) q.push_back(i);

    }
    while (!q.empty())
    {
        const int ci = q.front(); q.pop_front();
        answer.push_back(ci);
        for (const int ni : graph[ci])
        {
            indegree[ni]--;
            if (indegree[ni] == 0)
                q.push_back(ni);
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;
    graph.resize(N + 1);
    indegree.resize(N + 1);
    for (int i = 0; i < M; i++)
    {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        indegree[v]++;
    }

    bfs();
    for (auto v: answer) cout << v << ' ';
}
