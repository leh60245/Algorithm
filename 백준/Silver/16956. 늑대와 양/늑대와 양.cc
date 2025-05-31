#include <bits/stdc++.h>
using namespace std;
using vc = vector<char>;
using vvc = vector<vc>;
using pii = pair<int, int>;

vector<pii> dirt = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, C;
    cin >> R >> C;
    vvc grid(R, vc(C, ' '));
    vvc new_grid(R, vc(C, ' '));
    for (int r = 0; r < R; r++)
    {
        string s;
        cin >> s;
        for (int c = 0; c < C; c++)
        {
            grid[r][c] = s[c];
            new_grid[r][c] = s[c];
        }
    }

    for (int r = 0; r < R; r++)
    {
        for (int c = 0; c < C; c++)
        {
            if (grid[r][c] == 'S')
            {
                for (auto& [dr, dc] : dirt)
                {
                    int nr = r + dr, nc = c + dc;
                    if (nr < 0 || nr >= R || nc < 0 || nc >= C) continue;
                    if (grid[nr][nc] == 'W')
                    {
                        cout << 0;
                        return 0;
                    }
                    if (grid[nr][nc] != 'S')
                        new_grid[nr][nc] = 'D';
                }
            }
        }
    }
    cout << 1 << '\n';
    for (int r = 0 ; r < R ; r++)
    {
        for (int c = 0 ; c < C ; c++)
        {
            cout << new_grid[r][c];
        }
        cout << '\n';
    }
}
