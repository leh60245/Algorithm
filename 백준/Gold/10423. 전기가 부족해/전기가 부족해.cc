#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using tiii = tuple<int, int, int>;

int find(int x, vi& arr)
{
    if (arr[x] < 0)
        return x;
    return arr[x] = find(arr[x], arr);
}

bool uni(int u, int v, vi& arr)
{
    u = find(u, arr);
    v = find(v, arr);
    if (u == v)
        return false;
    if (arr[v] < arr[u])
        swap(u, v);
    if (arr[u] == arr[v])
        arr[u]--;
    arr[v] = u;
    return true;
}

/* 발전소는 이미 특정 도시에 건설되어 있고,
 * 따라서 추가적으로 드는 비용은 케이블을 설치할 때 드는 비용이 전부다.
 * [목표] 케이블 설치 비용 최소화
 * N개의 도시, M개의 캐이블 정보, K개의 발전소가 설치된 도시
 * 중요한점은, 어느 한 도시가 두 개의 발전소에서 전기를 공급받게 되면 낭비가 되므로,
 * 케이블이 연결된 도신에는 발전소가 반드시 하나만 존재해야 한다.
 */


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M, K; cin >> N >> M >> K;
    vi arr(N+1, -1);
    vector<tiii> costs;
    for (int k = 0 ; k < K ; k++)
    {
        int x; cin >> x;
        uni(x, 0, arr);
    }

    for (int m = 0 ; m < M ; m++)
    {
        int u, v, w; cin >> u >> v >> w;
        costs.emplace_back(w, u, v);
    }
    sort(costs.begin(), costs.end());


    int answer = 0;
    for (auto& [c, n1, n2] : costs)
    {
        if (!uni(n1, n2, arr)) continue;
        answer += c;
    }
    cout << answer;

}
