#include <bits/stdc++.h>

using namespace std;

int solution(vector<vector<int>> triangle) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int answer = 0;
    int N = triangle.size();
    vector<vector<int>> dp(N, vector<int>(N, 0));
    dp[0][0] = triangle[0][0];
    for (int i=1 ; i<N ; i++){
        for (int j=0; j < i+1 ; j++){
            if (j==0) dp[i][j] = dp[i-1][j] + triangle[i][j];
            else if (j==i) dp[i][j] = dp[i-1][j-1] + triangle[i][j];
            else {
                int tmp = max(dp[i-1][j], dp[i-1][j-1]);
                dp[i][j] = tmp + triangle[i][j];
            }
        }
    }
    for (int col = 0 ; col < N ; col++)
        if (dp[N-1][col] > answer) answer = dp[N-1][col];
    return answer;
}