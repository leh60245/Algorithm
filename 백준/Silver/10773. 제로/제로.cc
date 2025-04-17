#include <bits/stdc++.h>
using namespace std;


int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    stack<int> s;
    int k, cmd;
    cin >> k;
    while (k--)
    {
        cin >> cmd;
        if (cmd != 0) s.push(cmd);
        else s.pop();
    }
    int ans = 0;
    while (!s.empty()) {ans += s.top(); s.pop();}
    cout << ans;
}
