#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using pii = pair<int, int>;

bool DEBUG = false;

template <typename T>
void dbuge(const T& s)
{
    if (!DEBUG) return;
    cerr << s;
}

/* NxM의 세로선과 가로선
 * 세로선 사이에 가로선 놓을 수 있음. 놓을 수 있는 위치의 개수는 H
 * 가로선은 인접한 두 세로선을 연결해야 함. 단, 두 가로선이 연속하거나 서로 접하면 안됨
 *
 * 세로선 가장 위에서 아래 방향으로 내려감. 가로선 만나면 세로선 이동
 *
 * [목표] i번 세로선 결과가 i번이 나와야 한다.
 * 그러기 위해 '추가해야 하는 가로선 개수'의 최솟값 구하기.
 *
 * [입력]
 * N=세로선 개수, M=가로선 개수, H=가로선 놓을 수 있는 위치의 개수
 * 이후 M개의 줄에 '가로선의 정보'가 주어짐
 * 가로선 정보는 두 정수 a, b로 나타냄. b번 세로선과 b+1 세로선을 a번 점선 위치에 연결했다는 의미
 * (1, 1)에서 시작
 * 만약, 정답이 3보다 큰 값이거나, 불가능한 경우 -1을 출력
 */

int N, M, H;
vvi grid;
vector<pii> blank;
bool answer = false;

bool check()
{
    for (int col = 1; col <= N; col++)
    {
        int c_col = col;
        int row = 1;
        while (row <= H)
        {
            if (grid[row][c_col - 1])
                c_col -= 1;
            else if (grid[row][c_col])
                c_col += 1;
            row++;
        }
        if (c_col != col) return false;
    }
    return true;
}

void dfs(int max_depth, int cnt, int st)
{
    if (cnt == max_depth)
    {
        if (check())
            answer = true;
        return;
    }
    for (int i = st; i < blank.size(); i++)
    {
        auto [ci, cj] = blank[i];
        grid[ci][cj] = 1;
        dfs(max_depth, cnt + 1, i + 1);
        grid[ci][cj] = 0;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M >> H;
    grid.resize(H+2, vi(N+1, 0));
    for (int m = 0; m < M; m++)
    {
        int a, b;
        cin >> a >> b;
        grid[a][b] = 1;
    }
    for (int row = 1; row <= H; row++)
        for (int col = 1; col <= N; col++)
        {
            if (grid[row][col - 1] || grid[row][col] || grid[row][col + 1]) continue;
            blank.push_back({row, col});
        }

    for (int d = 0; d < 4; d++)
    {
        dbuge("start ");
        dbuge(to_string(d));
        dbuge("\n");
        dfs(d, 0, 0);
        if (answer)
        {
            cout << d;
            return 0;
        }
    }
    cout << -1;
    return 0;
}
