#include <bits/stdc++.h>
using namespace std;


int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    stack<int> s;
    int num;
    string cmd;
    cin >> num;
    while (num--)
    {
        cin >> cmd;
        if (cmd == "push")
        {
            int i;
            cin >> i;
            s.push(i);
        }
        else if (cmd == "pop")
        {
            if (!s.empty())
            {
                cout << s.top() << '\n';
                s.pop();
            }
            else
            {
                cout << -1 << '\n';
            }
        }
        else if (cmd == "size")
        {
            cout << s.size() << '\n';
        }
        else if (cmd == "empty")
        {
            if (!s.empty()) cout << 0 << '\n';
            else cout << 1 << '\n';
        }
        else // "top"
        {
            if (!s.empty())
            {
                cout << s.top() << '\n';
            }
            else
            {
                cout << -1 << '\n';
            }
        }
    }
}
