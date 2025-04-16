#include <bits/stdc++.h>
using namespace std;



int a[20], n, m;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    // 초기 설정
    for (int i=0;i<20;i++) a[i] = i+1;
    for (int i=0;i<10;i++)
    {
        cin >> n >> m;
        reverse(a+n-1, a+m);
    }
    for (auto &i : a) cout << i << ' ';
}
