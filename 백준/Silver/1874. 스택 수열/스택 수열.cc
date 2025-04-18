#include <bits/stdc++.h>
using namespace std;


int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    stack<int> s;
    list<char> result;
    int n, x, num=1, i=0;
    cin >> n;
    while (i < n)
    {
        cin >> x;
        // cout << x << " is input" << '\n';
        while (num<=n+1)
        {
            if (!s.empty() && s.top() == x)
            {
                s.pop();
                result.push_back('-');
                // cout << '-' << x << '\n';
                break;
            }
            s.push(num);
            result.push_back('+');
            // cout << '+' << s.top() <<'\n';
            num++;
        }
        i++;
    }
    if (!s.empty()) cout << "NO";
    else {for (char i:result) cout << i << '\n';}

}
