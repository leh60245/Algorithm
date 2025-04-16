#include <bits/stdc++.h>
using namespace std;

long long n, x, a;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> x;
    for (int i=0; i<n; i++)
    {
        cin >> a;
        if (a < x) cout << a << ' ';
    }
}
