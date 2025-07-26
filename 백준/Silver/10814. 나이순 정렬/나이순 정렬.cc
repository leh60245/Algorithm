#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;
    vector<pair<int, string>> user;
    for (int i = 0 ; i < N ; ++i) {
        int old; string name;
        cin >> old >> name;
        user.emplace_back(old, name);
    }
    stable_sort(user.begin(), user.end(), [](const auto &a, const auto &b) {
       return a.first < b.first;
    });

    for (auto [old, name] : user) {
        cout << old << ' ' << name << '\n';
    }

}