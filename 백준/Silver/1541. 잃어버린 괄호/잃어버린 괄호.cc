#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s; cin >> s;
    vector<int> num;
    vector<char> op;

    // 숫자와 연산자 분할하기
    int cur = 0;
    for (int i = 0 ; i < s.size() ; i++)
    {
        if ('0' <= s[i] && s[i] <= '9')
        {
            cur = cur * 10 + (s[i] - '0');
        } else
        {
            num.push_back(cur);
            op.push_back(s[i]);
            cur = 0;
        }
    }
    if (cur != 0) num.push_back(cur);
    // for (int i : num) cout << i << ' ';

    // 괄호 넣기
    int tmp = 0;
    int ans = num.front();
    for (int i=0; i<op.size(); i++)
    {
        if (op[i] == '+')
        {
            if (tmp != 0) tmp += num[i+1];
            else ans += num[i+1];
        } else
        {
            if (tmp != 0) ans -= tmp;
            tmp = num[i+1];
        }
    }
    if (tmp != 0) ans -= tmp;
    cout << ans;
}