// main.cpp
#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <algorithm>


using namespace std;

constexpr int INF = INT_MAX / 3;

struct Node {
    int vertex;
    int weight;
};

struct DijkstraResult {
    vector<int> cost;
    vector<int> prev;
};

using Graph = vector<vector<Node>>;

DijkstraResult dijkstra(int start, const Graph &graph) {
    vector<int> cost(graph.size(), INF);
    vector<int> prev(graph.size(), -1);
    auto cmp = [](const Node &a, const Node &b) {
        return a.weight > b.weight;
    };
    priority_queue<Node, vector<Node>, decltype(cmp)> pq(cmp);


    cost[start] = 0;
    pq.push({start, 0});

    while (!pq.empty()) {
        Node current = pq.top();
        pq.pop();
        int curVertex = current.vertex;
        int curWeight = current.weight;

        if (cost[curVertex] < curWeight) continue;
        for (const Node &next: graph[curVertex]) {
            int nxtVertex = next.vertex;
            int nxtWeight = next.weight;
            if (cost[nxtVertex] > cost[curVertex] + nxtWeight) {
                cost[nxtVertex] = cost[curVertex] + nxtWeight;
                prev[nxtVertex] = curVertex;
                pq.push({nxtVertex, cost[nxtVertex]});
            }
        }
    }
    return {cost, prev};
}

vector<int> restorePath(int start, int end, const vector<int> &prev) {
    vector<int> path;
    for (int at = end; at != -1; at = prev[at])
        path.push_back(at);

    reverse(path.begin(), path.end());
    if (path.front() != start) return {};
    return path;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int V, E;
    cin >> V >> E;

    Graph graph(V + 1);
    for (int i = 0; i < E; ++i) {
        int from, to, weight;
        cin >> from >> to >> weight;
        graph[from].push_back({to, weight});
    }

    int start, end;
    cin >> start >> end;

    auto [cost, prev] = dijkstra(start, graph);
    vector<int> path = restorePath(start, end, prev);
    cout << cost[end] << '\n';
    cout << path.size() << '\n';
    for (auto v : path) cout << v << ' ';

    return 0;
}
