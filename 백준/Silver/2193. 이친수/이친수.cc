#include <bits/stdc++.h>
using namespace std;

int N;
vector<vector<long long>> dp(91, vector<long long>(2, 0));

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    dp[1][0] = 0; dp[1][1] = 1;

    for (int i = 2; i<=N ; i++)
    {
        dp[i][0] = dp[i-1][0] + dp[i-1][1];
        dp[i][1] = dp[i-1][0];
    }
    cout << dp[N][0] + dp[N][1];


}