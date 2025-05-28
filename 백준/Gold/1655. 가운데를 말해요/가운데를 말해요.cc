#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;

int N;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> N;
    int v;
    priority_queue<int> left;
    priority_queue<int, vi, greater<int>> right;

    for (int i = 0; i < N; i++)
    {
        cin >> v;
        if (left.empty() || v <= left.top())
        {
            left.push(v);
        }
        else
        {
            right.push(v);
        }

        if (left.size() > right.size() + 1)
        {
            right.push(left.top());
            left.pop();
        }
        else if (right.size() > left.size())
        {
            left.push(right.top());
            right.pop();
        }

        cout << left.top() << '\n';
    }

    return 0;
}
