#include <bits/stdc++.h>
using namespace std;

/* 1 <= N <= 100
 * -100 <= v <= 100
 */

int a['z' - 'a' + 1], b['z' - 'a' + 1];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    list<char> arr = {};
    string s;
    cin >> s;
    for (auto i : s) arr.push_back(i);
    auto t = arr.end();

    int cmd_num;
    cin >> cmd_num;
    while (cmd_num--)
    {
        char c;
        cin >> c;
        if (c == 'L')
        {
            if (t != arr.begin()) t--;
        }
        else if (c == 'D')
        {
            if (t != arr.end()) t++;
        }
        else if (c == 'B')
        {
            if (t != arr.begin())
            {
                t--;
                t = arr.erase(t);
            }
        }
        else
        {
            char c2;
            cin >> c2;
            arr.insert(t, c2);
        }
    }
    for (char i:arr) cout << i;
}
