#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s; cin >> s;
    vi arr(26,0);
    for (char i : s)
    {
        if ('A' <= i && i <= 'Z') arr[i - 'A']++;
        else arr[i - 'a']++;
    }
    int max_value = arr[0];
    int max_idx = 0;
    int cnt = 1;
    for (int i = 1 ; i < arr.size() ; i++)
    {
        if (arr[i] > max_value)
        {
            max_value = arr[i];
            max_idx = i;
            cnt = 1;
        } else if (arr[i] == max_value)
        {
            cnt++;
        }
    }

    if (cnt > 1) cout << '?';
    else
    {
        char ans = 'A' + max_idx;
        cout << ans;
    }


}
