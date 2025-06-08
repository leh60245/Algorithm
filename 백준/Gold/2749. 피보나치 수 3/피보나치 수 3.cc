#include <bits/stdc++.h>
using namespace std;

using ll = long long;

constexpr int MOD = 1'000'000;
constexpr int PISANO = 1'500'000;
ll N;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    vector<ll> fib(PISANO);

    fib[0] = 0;
    fib[1] = 1;
    for (int i = 2; i < PISANO; i++)
        fib[i] = (fib[i - 1] + fib[i - 2]) % MOD;

    cout << fib[N % PISANO];
}
