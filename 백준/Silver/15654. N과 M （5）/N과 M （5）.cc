#include <bits/stdc++.h>
using namespace std;


int N, M;
vector<int> arr;
vector<int> ans;
vector<int> vis;

void permutation(int depth)
{
    if (depth == M)
    {
        for (int i = 0 ; i<M ; i++) cout << ans[i] << ' ';
        cout << '\n';
        return;
    }
    for (int n=0 ; n<N ; n++)
    {
        if (vis[n]) continue;
        vis[n] = 1;
        ans[depth] = arr[n];
        permutation(depth+1);
        vis[n] = 0;
    }

}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;
    arr.resize(N, 0);
    ans.resize(N, 0);
    vis.resize(N, 0);
    for (int n=0 ; n<N ; n++) cin >> arr[n];
    sort(arr.begin(), arr.end());

    permutation(0);
}
