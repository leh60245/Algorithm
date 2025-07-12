// main.cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
using vi = vector<int>;
using edge = tuple<int, int>;


int find(int x, vi &parents) {
    if (parents[x] < 0) return x;
    return parents[x] = find(parents[x], parents);
}

bool uni(int u, int v, vi &parents) {
    int pu = find(u, parents);
    int pv = find(v, parents);

    if (pu == pv) return false;
    if (parents[pu] == parents[pv]) parents[pu]--;
    if (parents[pu] < parents[pv]) parents[pv] = pu;
    else parents[pu] = pv;
    return true;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--){
        int N, M;
        cin >> N >> M;

        for (int i = 0 ; i < M ; i++){
            int a, b;
            cin >> a >> b;
        }
        
        cout << (N-1) << '\n';

    }


    return 0;
}
