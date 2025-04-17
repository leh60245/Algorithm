#include <bits/stdc++.h>
using namespace std;

/* 1 <= N <= 100
 * -100 <= v <= 100
 */

int a['z'-'a'+1], b['z'-'a'+1];
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    string n, m;
    cin >> n;
    for (char i : n) a[i-'a']++;
    cin >> m;
    for (char i : m) b[i-'a']++;
    int ans = 0;

    for (int i=0; i < 26 ; i++)
    {
        ans += max({a[i], b[i]}) - min({a[i], b[i]});
    }

    cout << ans;

}
