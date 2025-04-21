#include <bits/stdc++.h>
using namespace std;

bool DEBUG = false;
template<typename T>
void printGrid(const vector<vector<T>>& g , const string& name = "grid") {
    if (!DEBUG) return;
    cerr << name <<'\n';
    for (auto& row : g) {
        for (auto& val : row)
            cerr << val << ' ';
        cerr << '\n';
    }
}

int N, M, K;
vector<vector<int>> grid(21, vector<int>(21, 0));
array<int, 6> dice = {0,0,0,0,0,0}; // 아랫, 윗, 앞, 뒤, 오, 왼

void roll_dice(int cmd)
{
    auto [bottom, top, face, back, right, left] = dice;
    if (cmd == 1)
        dice = {right, left, face, back, top, bottom};
    else if (cmd == 2)
        dice = {left, right, face, back, bottom, top};
    else if (cmd == 3)
        dice = {back, face, bottom, top, right, left};
    else
        dice = {face, back, top, bottom, right, left};
}

unordered_map<int, pair<int, int>> dir = {
    {1, {0, 1}}, {2, {0, -1}}, {3, {-1, 0}}, {4, {1, 0}}
};

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int ci, cj;
    cin >> N >> M >> ci >> cj >> K;
    for (int i=0 ; i<N ; i++)
        for (int j=0; j<M ; j++)
            cin >> grid[i][j];
    printGrid(grid);
    for (int k=0; k<K ; k++)
    {
        if (DEBUG) cerr << "======== " << k+1 << " =============";
        int cmd; cin >> cmd;
        // 주사위 굴리기
        auto [di, dj] = dir[cmd];
        int ni = ci + di, nj = cj + dj;
        if (ni < 0 || N <= ni || nj < 0 || M <= nj) continue;
        ci = ni; cj = nj;
        roll_dice(cmd);
        // 주사위와 지도의 상호작용
        if (grid[ni][nj] == 0) grid[ni][nj] = dice[0];
        else
        {
            dice[0] = grid[ni][nj];
            grid[ni][nj] = 0;
        }

        cout << dice[1] << '\n';

    }

}