#include <bits/stdc++.h>
using namespace std;


int N, M;
vector<int> vis;
vector<int> arr;

void permutation(int depth)
{
    if (depth == M)
    {
        for (int i = 0 ; i<M ; i++) cout << arr[i] << ' ';
        cout << '\n';
        return;
    }
    int st = 1;
    if (depth != 0) st = arr[depth-1];
    for (int n=st ; n<=N ; n++)
    {
        arr[depth] = n;
        permutation(depth+1);
    }

}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;
    arr.resize(N, 0);
    permutation(0);
}
