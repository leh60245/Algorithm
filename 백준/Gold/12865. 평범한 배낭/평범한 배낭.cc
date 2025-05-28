#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;

int N, K; // N개의 물건, 최대 K만큼 무게 제한.

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> N >> K;
    vi weights(N);
    vi values(N);
    for (int i = 0; i < N; i++) cin >> weights[i] >> values[i];

    vi dp(K+1, 0);

    for (int i = 0 ; i < N ; i++)
        for (int w = K ; w >= weights[i] ; w--)
            dp[w] = max(dp[w], dp[w-weights[i]] + values[i]);

    cout << dp[K];
}
