#include <bits/stdc++.h>
using namespace std;

vector<int> days = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
vector<pair<int, int>> flowers;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N; cin >> N;
    while (N--)
    {
        int sm, sd, em, ed; cin >> sm >> sd >> em >> ed;
        flowers.push_back({sm*100+sd, em*100+ed});
    }

    int t = 301;
    int cnt = 0;
    while (t <= 1130)
    {
        int nt = t;
        for (auto [sd, ed]: flowers)
            if (sd <= t && nt < ed)
                nt = ed;
        if (t == nt)
        {
            cout << 0;
            return 0;
        }
        t = nt;
        cnt++;
    }
    cout << cnt;

    return 0;
}