#include <bits/stdc++.h>
using namespace std;


int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;
    stack<pair<int, int>> tower;
    tower.emplace(100000001, 0);
    for (int i=1; i<=N; i++)
    {
        int h;
        cin >> h;
        while (tower.top().first < h) tower.pop();
        cout << tower.top().second << " ";
        tower.emplace(h, i);
    }

}
