#include <bits/stdc++.h>
using namespace std;


int N, M;
vector<int> num;
vector<int> arr;
vector<int> vis;

void resize_all()
{
    num.resize(N, 0);
    arr.resize(N, 0);
    vis.resize(N, 0);
}

void permutation(int cnt)
{
    if (cnt == M)
    {
        for (int i = 0 ; i<M ; i++)
            cout << num[arr[i]] << ' ';
        cout << '\n';
        return;
    }
    int tmp = 0;
    for (int n=0 ; n<N ; n++)
    {
        if (tmp == num[n]) continue;
        // vis[n] = 1;
        arr[cnt] = n;
        tmp = num[n];
        permutation(cnt + 1);
        // vis[n] = 0;
    }

}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;
    resize_all();

    for (int n=0 ; n<N ; n++) cin >> num[n];
    sort(num.begin(), num.end());

    permutation(0);
}
