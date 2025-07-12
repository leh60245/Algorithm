// main.cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <queue>

#define INF (INT_MAX/3)
#define cost first
#define node second

using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;

int V, E, K;
vector<vector<pair<int, int>>> adj;
vi dist;
priority_queue<pair<int, int>,
        vector<pair<int, int>>,
        greater<>> pq;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> V >> E >> K;
    adj.resize(V + 1);
    dist.resize(V + 1, INF);
    dist[K] = 0;
    for (int i = 0; i < E; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].emplace_back(w, v);
    }

    pq.emplace(dist[K], K);
    while (!pq.empty()) {
        auto cur = pq.top();
        pq.pop();
        if (dist[cur.node] != cur.cost) continue;
        for (auto nxt: adj[cur.node]) {
            if (dist[nxt.node] <= dist[cur.node] + nxt.cost) continue;
            dist[nxt.node] = dist[cur.node] + nxt.cost;
            pq.emplace(dist[nxt.node], nxt.node);
        }
    }
    for (int i = 1; i <= V; i++) {
        if (dist[i] == INF) cout << "INF\n";
        else cout << dist[i] << "\n";
    }

    return 0;
}
