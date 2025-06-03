#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;

int N, a, b;
vi grid;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> a >> b;

    // 조건에 맞는 경우가 없음
    if (a + b - 1 > N)
    {
        cout << -1;
        return 0;
    }
    if (a > 1)
        for (int i = 0 ; i < (N - (a+b-1)) ; i++)
            grid.push_back(1);
    for (int i = 1; i < a; i++)
        grid.push_back(i);
    grid.push_back(max({a, b}));
    if (a == 1)
        for (int i = 0 ; i < (N - (a+b-1)) ; i++)
            grid.push_back(1);
    for (int i = b - 1; i > 0; i--)
        grid.push_back(i);



    for (auto& v : grid) cout << v << ' ';
}
