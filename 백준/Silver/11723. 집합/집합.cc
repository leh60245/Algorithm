#include <bits/stdc++.h>
using namespace std;

int M;
set<int> arr;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> M;
    string cmd;
    while (M--)
    {
        cin >> cmd;
        int v;
        if (cmd == "add") {
            cin >> v;
            arr.insert(v);
        } else if (cmd == "remove") {
            cin >> v;
            arr.erase(v);
        } else if (cmd == "check") {
            cin >> v;
            cout << (arr.count(v) ? 1 : 0) << '\n';
        } else if (cmd == "toggle") {
            cin >> v;
            if (arr.count(v)) arr.erase(v);
            else arr.insert(v);
        } else if (cmd == "all") {
            for (int i = 1 ; i <= 20 ; i++)
                arr.insert(i);
        } else if (cmd == "empty") {
            arr.clear(); 
        }
    }
}
