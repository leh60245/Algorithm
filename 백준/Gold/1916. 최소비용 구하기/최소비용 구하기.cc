// main.cpp
/*
최소비용 구하기
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.5 초	128 MB	118815	40536	26894	33.249%
문제
N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다.
 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다.
 A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.

입력
첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)이 주어지고 둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)이 주어진다. 그리고 셋째 줄부터 M+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.

그리고 M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다. 출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.

출력
첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.

예제 입력 1
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
예제 출력 1
4
 */
#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

constexpr int INF = INT_MAX / 3;

struct Node {
    int vertex;
    int weight;
};

using Cost = vector<int>;
using Graph = vector<vector<Node>>;

Cost dijkstra(int start, Graph &graph) {
    auto cmp = [](const Node &a, const Node &b) {
        return a.weight > b.weight;
    };
    priority_queue<Node, vector<Node>, decltype(cmp)> pq(cmp);
    Cost cost((int) graph.size(), INF);

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



    int N, M ; cin >> N >> M;
    Graph graph(N+1);
    for (int i = 0 ; i < M ; ++i){
        int from, to, cost;
        cin >> from >> to >> cost;
        graph[from].push_back({to, cost});
    }

    int start, end;
    cin >> start >> end;
    Cost cost = dijkstra(start, graph);

    cout << cost[end];

    return 0;
}
