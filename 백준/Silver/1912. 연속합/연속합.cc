#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N; cin >> N;
    vector<int> dp(100001, 0);
    vector<int> ar(100001, 0);
    for (int i=1; i<=N ; i++) cin >> ar[i];

    for (int i=1; i<=N ; i++)
        dp[i] = max(dp[i-1], 0) + ar[i];

    cout << *max_element(dp.begin()+1, dp.begin()+N+1);
}