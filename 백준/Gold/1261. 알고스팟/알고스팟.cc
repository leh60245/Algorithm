// main.cpp
#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <string>
#include <unordered_map>

using namespace std;

constexpr int INF = INT_MAX / 3;

struct Node {
    int vertex;
    int weight;
};

using Cost = unordered_map<int, int>;
using Graph = unordered_map<int, vector<Node>>;

Cost dijkstra(int start, Graph &graph) {
    auto cmp = [](const Node &a, const Node &b) {
        return a.weight > b.weight;
    };
    priority_queue<Node, vector<Node>, decltype(cmp)> pq(cmp);
    Cost cost;
    for (auto& [key, _] : graph){
        cost[key] = INF;
    }

    cost[start] = 0;
    pq.push({start, 0});

    while (!pq.empty()) {
        auto current = pq.top();
        pq.pop();
        if (cost[current.vertex] < current.weight) continue;
        for (auto next: graph[current.vertex]) {
            if (cost[next.vertex] > cost[current.vertex] + next.weight) {
                cost[next.vertex] = cost[current.vertex] + next.weight;
                pq.push({next.vertex, cost[next.vertex]});
            }
        }
    }

    return cost;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int M, N ; cin >> M >> N;
    vector<vector<int>> grid(N, vector<int>(M, 0));
    for (int i = 0 ; i < N ; ++i){
        string input ; cin >> input;
        for (int j = 0 ; j < M ; ++j){
            grid[i][j] = input[j] - '0';
        }
    }

    Graph graph;
    vector<pair<int, int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    for (int i = 0 ; i < N ; ++i){
        for (int j = 0 ; j < M ; ++j){
            for (auto [di, dj] : dirs) {
                int ni = i + di, nj = j + dj;
                if (ni < 0 || ni >= N || nj < 0 || nj >= M) continue;
                int cost = grid[ni][nj];
                graph[i*M + j].push_back({ni*M + nj, cost});
            }
        }
    }

    Cost cost = dijkstra(0, graph);
    cout << cost[(N-1) * M + (M-1)];
    return 0;
}