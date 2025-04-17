#include <bits/stdc++.h>
using namespace std;

/* 1 <= N <= 100
 * -100 <= v <= 100
 */

int N, v;
int a[101];
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    for (int i=0; i < N; i++) cin >> a[i];
    cin >> v;

    int ans = 0;
    for (int i=0; i<N; i++)
    {
        if (a[i] == v) ans++;
    }
    cout << ans;


}
