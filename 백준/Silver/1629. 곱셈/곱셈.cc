#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int A, B, C;

ll power(ll b)
{
    if (b == 0) return 1;
    if (b == 1) return A % C;

    ll k = power(b/2) % C;
    if (b % 2 == 0) return k * k % C;
    return k * k % C * A % C;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> A >> B >> C;
    cout << power(B);
}
