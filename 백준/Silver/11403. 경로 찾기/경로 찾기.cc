#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;

#define DEBUG true

int N;
vvi graph;

template <typename T>
void printGrid(const vector<vector<T>>& grid, const string& name = "Grid")
{
    if constexpr (!DEBUG)
        return;
    cout << "===== " << name << " =====\n";
    for (const auto& row : grid)
    {
        for (const auto& val : row)
        {
            cout << val << ' ';
        }
        cout << '\n';
    }
    cout << '\n';
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    graph.resize(N, vi(N, 0));
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cin >> graph[i][j];

    for (int k = 0; k < N; k++)
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                if (graph[i][k] && graph[k][j])
                    graph[i][j] = 1;

    for (int i = 0 ; i < N ; i++)
    {
        for (int j = 0 ; j < N ; j++)
        {
            cout << graph[i][j] << ' ';
        }
        cout << '\n';
    }
}
