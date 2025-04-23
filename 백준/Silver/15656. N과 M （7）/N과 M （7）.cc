#include <bits/stdc++.h>
using namespace std;


int N, M;
vector<int> num;
vector<int> arr;
// vector<int> vis;

void resize_all()
{
    num.resize(N, 0);
    arr.resize(N, 0);
    // vis.resize(N, 0)
}

void permutation(int depth)
{
    if (depth == M)
    {
        for (int i = 0 ; i<M ; i++)
            cout << num[arr[i]] << ' ';
        cout << '\n';
        return;
    }
    int st = 0;
    // if (depth != 0) st = arr[depth-1];
    for (int n=st ; n<N ; n++)
    {
        arr[depth] =n;
        permutation(depth+1);
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
