#include <bits/stdc++.h>
using namespace std;


int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);


    deque<int> q;
    int N, M;
    cin >> N >> M;
    for (int i=1; i<=N ; i++) q.push_back(i);

    int ans = 0;
    while (M--)
    {
        int num;
        cin >> num;

        int idx = find(q.begin(), q.end(), num) - q.begin();
        while (q.front() != num)
        {
            ans++;
            if (idx > q.size() - idx)
            {
                q.push_front(q.back());
                q.pop_back();
            } else
            {
                q.push_back(q.front());
                q.pop_front();
            }
        }
        q.pop_front();
    }
    cout << ans;
}
