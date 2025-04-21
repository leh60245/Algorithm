#include <bits/stdc++.h>
using namespace std;

vector<long long> arr(100001);
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N; cin >> N ;
    long long M; cin >> M;
    for (int n=0; n<N; n++) cin >> arr[n];

    sort(arr.begin(), arr.begin()+N);
    int ep = 0;
    long long ans = 2000000001;
    for (int sp=0; sp<N; sp++)
    {
        while (ep < N && arr[ep] - arr[sp] < M) ep++;
        if (ep >= N) break;
        ans = min({ans, arr[ep] - arr[sp]});
        if (ans == M)
        {
            cout << M; return 0;
        }
    }
    cout << ans;
    return 0;
}