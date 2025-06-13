#include <bits/stdc++.h>
using namespace std;
#define DEBUG true;

int N;
vector<int> arr;
vector<int> dp;


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    arr.resize(N, 0);
    dp.resize(N, 1);
    for (int i = 0 ; i < N ; ++i) cin >> arr[i];
    for (int i = 1 ; i < N ; ++i)
        for (int j = 0 ; j < i ; ++j)
            if (arr[j] < arr[i])
                dp[i] = max(dp[i], dp[j] + 1);

    cout << *max_element(dp.begin(), dp.end());
}
