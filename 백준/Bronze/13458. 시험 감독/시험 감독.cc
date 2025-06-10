#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;
using pii = pair<int, int>;
using ll = long long;

ll N, B, C;
vector<ll> arr;
ll ans = 0;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> N;
    arr.resize(N, 0);
    for (int i = 0 ; i < N ; i++) cin >> arr[i];
    cin >> B >> C;
    for (int i = 0 ; i < N ; i++)
    {
        ll v = arr[i];
        v -= B;

        ans++;
        if (v > 0)
        {
            ans +=  v / C;
            if (v % C > 0) ans++;

        }

    }
    cout << ans;
}