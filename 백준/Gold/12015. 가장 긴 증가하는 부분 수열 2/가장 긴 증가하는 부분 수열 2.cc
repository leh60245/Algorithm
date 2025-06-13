#include <bits/stdc++.h>
using namespace std;
#define DEBUG true;

int N;
vector<int> arr;


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    arr.resize(N, 0);
    for (int i = 0; i < N; ++i)
        cin >> arr[i];

    vector<int> lis;
    for (int i = 0; i < N; ++i) {
        int x = arr[i];
        auto it = lower_bound(lis.begin(), lis.end(), x);
        if (it == lis.end()) {
            lis.push_back(x);
        }
        else {
            *it = x;
        }
    }

    cout << lis.size() << '\n';
}
