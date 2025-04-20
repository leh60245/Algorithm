#include <bits/stdc++.h>
using namespace std;

int N;
vector<int> dp(1001, 0);

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    dp[0] = 1; dp[1] = 3;
    for (int i=2; i< N ; i++)
    {
        dp[i] = dp[i-1] + 2*dp[i-2];
        dp[i] %= 10007;
    }
    cout << dp[N-1];

}