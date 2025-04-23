#include <bits/stdc++.h>
using namespace std;


int N, M;
vector<int> vis;

void permutation(int depth, vector<int>& path)
{
    if (depth == M)
    {
        for (auto v : path) cout << v << ' ';
        cout << '\n';
        return;
    }
    for (int n=1 ; n<=N ; n++)
        if (!vis[n])
        {
            vis[n] = 1;
            path.push_back(n);
            permutation(depth+1, path);
            path.pop_back();
            vis[n] = 0;
        }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;
    vis.resize(N+1, 0);
    vector<int> path = {};
    permutation(0, path);

}
