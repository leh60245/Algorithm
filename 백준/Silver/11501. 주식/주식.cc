#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T; cin >> T;
    while (T--)
    {
        int N; cin >> N;
        int arr[N];
        for (int n=0 ; n<N ; n++)
        {
            int x; cin >> x;
            arr[n] = x;
        }
        long ans = 0;
        int max_value = arr[N-1];
        for (int i=N-2; i >= 0 ; i--)
        {
            if (arr[i] > max_value) max_value = arr[i];
            else if (arr[i] < max_value)
            {
                ans += (max_value - arr[i]);
            }
        }
        cout <<  ans << '\n';
    }
}