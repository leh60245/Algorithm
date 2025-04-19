#include <bits/stdc++.h>
using namespace std;


int N, M; // 사람 수, 파티 수
int know[52];
vector<int> party[52];
vector<int> graph[52];

void bfs()
{
    deque<int> q;
    for (int i=1; i<=N; i++)
        if (know[i]) q.push_back(i);

    while (!q.empty())
    {
        int cur = q.front(); q.pop_front();
        for (int nxt: graph[cur])
        {
            if (know[nxt]) continue;
            q.push_back(nxt);
            know[nxt] = 1;
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N >> M;

    int know_num; cin >> know_num; // 알고있는 사람 수
    while (know_num--)
    {
        int x; cin >> x;
        know[x] = 1;
    }

    for (int p=1; p <= M ; p++)
    {
        int num; cin >> num; // p번째 파티 참여 사람 수

        int prv; cin >> prv;
        party[p].push_back(prv);

        while (--num)
        {
            int nxt; cin >> nxt;
            party[p].push_back(nxt);
            graph[prv].push_back(nxt);
            graph[nxt].push_back(prv);
            swap(prv, nxt);
        }
    }

    bfs(); // 아는 사람들 찾기

    int ans = 0;
    for (int p=1; p<=M; p++)
    {
        bool is_okay = true;
        for (int num: party[p])
        {
            if (know[num])
            {
                is_okay=false;
                break;
            }
        }
        if (is_okay) ans++;
    }
    cout << ans;
}



