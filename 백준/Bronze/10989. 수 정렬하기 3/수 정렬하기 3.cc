#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int N; cin >> N;
    vi arr(10001, 0);
    while (N--)
    {
        int x; cin >> x;
        arr[x] += 1;
    }
    for (int i = 1 ; i <= 10000 ; i++)
    {
        for (int j = 0 ; j < arr[i] ; j++)
        {
            cout << i << '\n';
        }
    }

}
