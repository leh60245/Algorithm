#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;
using vs = vector<string>;
using pqs = priority_queue<string, vector<string>, greater<>>;

int N, M; // 사람 수, 정보 수
vs names;
unordered_map<string, vs> information;
unordered_map<string, int> indegree;

vs older;
unordered_map<string, pqs> graph;

void bfs()
{
    deque<string> q; // {부모, 자식}

    for (auto& [name, num] : indegree)
    {
        if (num == 0)
        {
            q.push_back(name);
            older.push_back(name);
        }
    }
    while (!q.empty())
    {
        const string& name = q.front(); q.pop_front();
        for (auto& child : information[name])
        {
            indegree[child]--;
            if (indegree[child] == 0)
            {
                graph[name].push(child);
                q.push_back(child);
            }
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    for (int i = 0; i < N; i++)
    {
        string name;
        cin >> name;
        names.push_back(name);
        information[name] = {};
        indegree[name] = 0;
    }
    cin >> M;
    for (int m = 0; m < M; m++)
    {
        string child, parents;
        cin >> child >> parents;
        information[parents].push_back(child);
        indegree[child]++;
    }

    bfs();

    // 출력부분
    cout << older.size() << '\n';
    sort(older.begin(), older.end());
    for (const string& name : older) cout << name << ' ';
    cout << '\n';

    sort(names.begin(), names.end());
    for (const string& name : names)
    {
        cout << name << ' '; // 이름 출력
        cout << graph[name].size() << ' ';
        while (!graph[name].empty())
        {
            cout << graph[name].top() << ' ';
            graph[name].pop();
        }
        cout << '\n';
    }
}
