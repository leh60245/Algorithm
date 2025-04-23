#include <bits/stdc++.h>
using namespace std;


int N, M;
vector<int> arr;
vector<int> ans;
// vector<int> vis;

void resize_all()
{
    arr.resize(N, 0);
    ans.resize(N, 0);
    // vis.resize(N, 0)
}

void permutation(int depth)
{
    if (depth == M)
    {
        for (int i = 0 ; i<M ; i++) cout << ans[i] << ' ';
        cout << '\n';
        return;
    }
    int base = arr[0];
    if (depth != 0) base = ans[depth-1];
    for (int n=0 ; n<N ; n++)
    {
        if (depth >0 && arr[n] <= base) continue;
        ans[depth] = arr[n];
        permutation(depth+1);
    }

}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;
    resize_all();

    for (int n=0 ; n<N ; n++) cin >> arr[n];
    sort(arr.begin(), arr.end());

    permutation(0);
}
