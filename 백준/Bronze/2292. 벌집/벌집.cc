#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;

/*
 * 1, 6, 12, 18
 */

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N; cin >> N;
    long long tmp = 1;
    int cnt = 1;
    while (tmp < N)
    {
        tmp += 6 * cnt;
        cnt++;
    }
    cout << cnt;

}
