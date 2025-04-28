#include <bits/stdc++.h>
using namespace std;

/* N개 문제. 문제는 난이도 순서로 출제. 쉬움 1번 ~ 어려움 N번
 * 문제마다 먼저 풀면 좋은 문제가 있음.
 *
 * [문제 풀 순서 정하기]
 * 1. N개 문제 모두 풀어야 함.
 * 2. 먼저 푸는 것이 좋은 문제가 있는 문제는, 먼저 푸는 것이 좋은 문제를 반드시 먼저 푼다.
 * 3. 가능하면 쉬운 문제부터 푼다.
 *
 * [목표] 문제 순서 결정
 */

using vi = vector<int>;
using vvi = vector<vi>;
using pqi = priority_queue<int, vi, greater<>>;

int N, M;
vvi graph;
vi indegree;
vi result;

void bfs()
{
    pqi q;

    for (int i = 1; i <= N; i++)
        if (indegree[i] == 0) q.push(i);

    while (!q.empty())
    {
        int cn = q.top();
        q.pop();
        result.push_back(cn);
        for (const int& nn : graph[cn])
        {
            indegree[nn]--;
            if (indegree[nn] == 0)
                q.push(nn);
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> N >> M;
    graph.resize(N+1);
    indegree.resize(N + 1);
    for (int m = 0; m < M; m++)
    {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        indegree[b]++;
    }

    bfs();

    for (auto& v : result) cout << v << ' ';
}
