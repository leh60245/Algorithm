#include <bits/stdc++.h>
using namespace std;

int N;
vector<vector<int>> dp(502, vector<int>(502, 0));

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    int x; cin >> x; // 초기값
    dp[0][0] = x;
    for (int i=1; i<N; i++)
    {
        for (int j=0 ; j<i+1; j++)
        {
            cin >> x;
            if (j == 0) dp[i][j] = dp[i-1][j] + x;
            else dp[i][j] = max({dp[i-1][j-1], dp[i-1][j]}) + x;
        }
    }
    cout << *max_element(dp[N-1].begin(), dp[N-1].end());
}