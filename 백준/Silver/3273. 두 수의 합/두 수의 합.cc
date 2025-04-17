#include <bits/stdc++.h>
using namespace std;


int a[100001];
bool c[2000001];
int n, x;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int ans = 0;
    cin >> n;
    for (int i=0; i<n; i++) cin >> a[i];
    cin >> x;

    for (int i=0; i<n; i++)
    {
        if (x-a[i] > 0 && c[x-a[i]]) ans++;
        c[a[i]] = true;
    }
    cout << ans;

}
