#include <bits/stdc++.h>
#define DEBUG false
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;
using pii = pair<int, int>;
using tiii = tuple<int, int, int>;

int N, M;
vvi grid, tmp;
int di[4] = {0, 1, 0, -1};
int dj[4] = {1, 0, -1, 0};
vector<tiii> bridge;
vector<int> parent;
int totalCost = 0, totalConnect = 0;

template <typename T>
void printGrid(vector<vector<T>>& grid, const string& name = "Grid") {
    if (!DEBUG)
        return;
    cout << name << '\n';
    for (int i = 0; i < grid.size(); ++i) {
        for (int j = 0; j < grid[i].size(); ++j) {
            cout << grid[i][j] << ' ';
        }
        cout << '\n';
    }
    cout << '\n';
}

bool oob(const int i, const int j) { return (i < 0 || i >= N || j < 0 || j >= M); }

void bfs(const int si, const int sj, const int numbering) {
    deque<pii> q;

    q.emplace_back(si, sj);
    grid[si][sj] = numbering;

    while (!q.empty()) {
        auto& [ci, cj] = q.front();
        q.pop_front();
        for (int d = 0; d < 4; ++d) {
            int ni = ci + di[d], nj = cj + dj[d];
            if (oob(ni, nj))
                continue;
            if (tmp[ni][nj] != 1 || grid[ni][nj])
                continue;

            q.emplace_back(ni, nj);
            grid[ni][nj] = numbering;
        }
    }
}

void makeBridge() {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (!grid[i][j])
                continue;
            int fromNumber = grid[i][j];
            for (int d = 0; d < 4; ++d) {
                int ni = i, nj = j, length = 0;
                while (true) {
                    ni += di[d];
                    nj += dj[d];
                    if (oob(ni, nj))
                        break;

                    if (grid[ni][nj] == fromNumber)
                        break;

                    if (grid[ni][nj] == 0)
                        ++length;
                    else {
                        if (length >= 2) {
                            int toNumber = grid[ni][nj];
                            bridge.emplace_back(length, min(fromNumber, toNumber), max(fromNumber, toNumber));
                        }
                        break;
                    }
                }
            }
        }
    }
}

int find(const int& x) {
    if (parent[x] < 0)
        return x;
    return parent[x] = find(parent[x]);
}

bool uni(int x, int y) {
    x = find(x);
    y = find(y);
    if (x == y)
        return false;
    if (parent[x] == parent[y])
        parent[x]--;
    if (parent[x] < parent[y])
        parent[y] = x;
    else
        parent[x] = y;
    return true;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;
    grid.resize(N, vi(M, 0));
    tmp.resize(N, vi(M, 0));


    for (int i = 0; i < N; ++i)
        for (int j = 0; j < M; ++j)
            cin >> tmp[i][j]; // 0은 바다, 1은 땅

    // [1] 그룹 짓기
    int numbering = 0;
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < M; ++j) {
            if (tmp[i][j] == 0 || grid[i][j] > 0)
                continue;
            numbering++;
            bfs(i, j, numbering);
        }
    printGrid(grid);

    // [2] 다리 잇기
    parent.resize(numbering + 1, -1);
    makeBridge();

    // [3] 최소 거리 구하기
    sort(bridge.begin(), bridge.end());
    for (auto& [cost, u, v] : bridge) {
        if (!uni(u, v))
            continue;
        totalCost += cost;
        ++totalConnect;
        if (totalConnect == numbering - 1)
            break;
    }

    if (totalConnect == numbering - 1)
        cout << totalCost;
    else
        cout << -1;

}
