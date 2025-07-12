// main.cpp
#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>

using namespace std;
using vi = vector<int>;
using Edge = tuple<int, int, int>; // (cost, a, b)

int V, E;
vector<Edge> edges;
vi parent;

int find(int x) {
    if (parent[x] < 0) return x;
    return parent[x] = find(parent[x]);
}


bool unite(int u, int v) {
    int pu = find(u), pv = find(v);
    if (pu == pv) return false; 

    if (parent[pu] == parent[pv]) parent[pu]--;
    if (parent[pu] < parent[pv])
        parent[pv] = pu;
    else
        parent[pu] = pv;
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> V >> E;
    edges.reserve(E);
    parent.assign(V + 1, -1); 

    for (int i = 0; i < E; ++i) {
        int a, b, cost;
        cin >> a >> b >> cost;
        edges.emplace_back(cost, a, b);
    }

    sort(edges.begin(), edges.end()); 

    long long totalCost = 0;
    for (const auto& [cost, a, b] : edges) {
        if (unite(a, b)) {
            totalCost += cost;
        }
    }

    cout << totalCost << '\n';
    return 0;
}
