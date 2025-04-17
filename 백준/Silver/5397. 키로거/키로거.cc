#include <bits/stdc++.h>
using namespace std;


int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    string s;



    cin >> n;
    while (n--)
    {
        list<char> pw;
        auto h = pw.end();
        cin >> s;
        for (char c : s)
        {
            if (c == '<')
            {
                if (h != pw.begin()) h--;
            }
            else if (c == '>')
            {
                if (h != pw.end()) h++;
            }
            else if (c == '-')
            {
                if (h != pw.begin())
                {
                    h--;
                    h = pw.erase(h);
                }
            }
            else
            {
                pw.insert(h, c);
            }
        }
        for (char c: pw) cout << c;
        cout << '\n';
    }
}
