#include <bits/stdc++.h>
using namespace std;



int a[5];
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    for (int & i : a)
    {
       cin >> i;
    }
    int sum = 0;
    if (a[0] < 0)
    {
        sum -= a[0] * a[2];
        sum += a[3];
        sum += a[4] * a[1];
        cout << sum;
        return 0;
    } else
    {
        sum += (a[1] - a[0]) * a[4];
        cout << sum;
        return 0;
    }
}
