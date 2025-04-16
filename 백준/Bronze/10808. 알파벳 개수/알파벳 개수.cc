#include <bits/stdc++.h>
using namespace std;



int num[((int) 'z')-((int) 'a')+1];
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    string s;
    cin >> s;
    for (int i=0;i<s.size();i++) num[((int) s[i]) - ((int) 'a')] ++;
    for (int i : num) cout << i << ' ';

}
