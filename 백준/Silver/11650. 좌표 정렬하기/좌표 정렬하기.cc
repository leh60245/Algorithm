#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;
    vector<pair<int, int> > point;
    for (int i = 0; i < N; ++i) {
        int x, y;
        cin >> x >> y;
        point.emplace_back(x, y);
    }
    stable_sort(point.begin(), point.end(), [](const auto &a, const auto &b) {
        if (a.first == b.first) return a.second < b.second;
        return a.first < b.first;
    });

    for (auto [x, y]: point) {
        cout << x << ' ' << y << '\n';
    }
}
