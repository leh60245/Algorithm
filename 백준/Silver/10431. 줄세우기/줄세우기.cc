#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int x;
        cin >> x;
        int answer = 0;
        vector<int> arr(20, 0);
        for (int i = 0; i < 20; i++) {
            int v; cin >> v;
            for (int j = 0; j < i; j++)
                if (v < arr[j])
                    answer++;
            arr[i] = v;
        }
        cout << t << ' ' << answer << '\n';
    }
}
