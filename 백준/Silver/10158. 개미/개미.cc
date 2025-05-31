#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;

int w, h;
int p, q;
int t;

bool oob(int i, int j)
{
    return (i < 0 || i > w || j < 0 || j > h);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> w >> h;
    cin >> p >> q;
    cin >> t;

    int tp = (p + t) / w;
    int cp;
    if (tp % 2 == 1) cp = w - ((p + t) % w);
    else cp = (p + t) % w;

    int tq = (q + t) / h;
    int cq;
    if (tq % 2 == 1) cq = h - ((q + t) % h);
    else cq = (q + t) % h;

    cout << cp << ' ' << cq;
}
