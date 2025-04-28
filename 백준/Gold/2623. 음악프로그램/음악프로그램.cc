#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;


int N, M;
vvi graph;
vi indegree;
vi answer;


bool bfs()
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
    for (const int ind : indegree)
        if (ind != 0) return false;

    return true;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;
    graph.resize(N + 1);
    indegree.resize(N + 1);
    for (int m = 0 ; m < M ; m++)
    {
        int sz ; cin >> sz;
        int h; cin >> h;
        for (int i = 1 ; i < sz ; i++)
        {
            int t; cin >> t;
            graph[h].push_back(t);
            indegree[t]++;
            h = t;
        }
    }
    bool can_answer = bfs();
    if (can_answer) for (const int v : answer) cout << v << '\n';
    else cout << 0;
}
