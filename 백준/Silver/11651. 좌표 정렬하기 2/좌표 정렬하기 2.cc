#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int N; cin >> N;
    vector<pair<int, int>> arr(N);
    for (int i = 0 ; i < N ; i++) cin >> arr[i].first >> arr[i].second;
    sort(arr.begin(), arr.end(), [](const auto& a, const auto& b)
    {
        if (a.second != b.second) return a.second < b.second;
        return a.first < b.first;
    });
    for (int i = 0 ; i < N ; i++) cout << arr[i].first << ' ' << arr[i].second << '\n';

}
