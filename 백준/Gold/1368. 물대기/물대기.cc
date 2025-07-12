// main.cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
using vi = vector<int>;
using edge = tuple<int, int, int>;

int N;
vector<edge> edges;
vi parents;

int find(int x) {
    if (parents[x] < 0) return x;
    return parents[x] = find(parents[x]);
}

bool uni(int u, int v) {
    int pu = find(u);
    int pv = find(v);

    if (pu == pv) return false;
    if (parents[pu] == parents[pv]) parents[pu]--;
    if (parents[pu] < parents[pv]) parents[pv] = pu;
    else parents[pu] = pv;
    return true;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    parents.resize(N + 1, -1);

    for (int i = 1; i <= N ; i++) {
        int w;
        cin >> w;
        edges.emplace_back(w, i, 0);
    }
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            int cost;
            cin >> cost;
            if (i >= j) continue;
            edges.emplace_back(cost, i, j);
        }
    }

    sort(edges.begin(), edges.end());

    int ans = 0;
    for (auto [cost, a, b]: edges) {
        if (!uni(a, b)) continue;
        ans += cost;
    }

    cout << ans;
    return 0;
}
