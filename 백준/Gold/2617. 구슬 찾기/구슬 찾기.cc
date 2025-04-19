#include <bits/stdc++.h>
using namespace std;

/* 모양은 같고, 무게가 모두 다른 N개의 구슬
 * N은 홀수, 구슬마다 번호가 1~N 붙어 있음.
 * 무게가 전체의 중간인 (무게 순서로 (N+1)/2 번째) 구슬을 찾기 위해 아래 일을 함
 *
 * 주어진 건 양팔 저울. 한 쌍의 구슬을 골라 양팔 저울 양쪽에 하나씩 올려 어느 쪽이 무거운지 알 수 있음
 * 이렇게 M개 쌍을 골라 각각 양팔저울에 올려 어느 것이 무거운가 모두 알아냄
 * 이 결과를 이용해 무게가 중간이 될 가능성이 전혀 없는 구슬들을 먼저 제외함
 *
 * 무거운거 결과는 주어짐
 * 중간 무게 구슬은 구할 순 없지만, 절대 될 수 없는 구슬들은 찾을 수 있음
 *
 * [목표] 무게가 중간인 구슬이 될 수 없는 구슬 개수를 구하여라.
 */

int N, M;
vector<int> heavy_graph[100], light_graph[100];
bool vis[100];

int bfs(int si)
{
    memset(vis, false, sizeof(vis));
    deque<int> q;
    int cnt = 0;

    q.push_back(si);
    while (!q.empty())
    {
        auto ci = q.front(); q.pop_front();

        for (int ni: heavy_graph[ci])
        {
            if (vis[ni]) continue;
            q.push_back(ni);
            vis[ni] = true;
            cnt++;
        }
    }
    if (cnt >= ((N+1)/2)) return 1;
    memset(vis, false, sizeof(vis));
    q.clear();
    cnt = 0;

    q.push_back(si);
    while (!q.empty())
    {
        auto ci = q.front(); q.pop_front();

        for (int ni: light_graph[ci])
        {
            if (vis[ni]) continue;
            q.push_back(ni);
            vis[ni] = true;
            cnt++;
        }
    }
    if (cnt >= ((N+1)/2)) return 1;
    return 0;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;
    while (M--)
    {
        int u, v;
        cin >> u >> v;
        heavy_graph[u].push_back(v);
        light_graph[v].push_back(u);
    }

    int ans = 0;
    for (int n=1 ; n<=N ; n++)
    {
        ans += bfs(n);
    }

    cout << ans;
}
