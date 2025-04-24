#include <bits/stdc++.h>

using namespace std;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using pii = pair<int,int>;

bool DEBUG = true;
/* nxm 크기 격자판 퍼즐
* 빨간 수래, 파란 수래 하나씩. 각 수레들은 자신의 시작 칸부터 도착 칸까지 이동해야 함. 
* 모든 수레들을 각자 도착 칸으로 이동시키면 퍼즐 풀 수 있음
* [턴]
* 각 턴마다 모든 수레를 '반드시' 상하좌우 인접 한 칸으로 움직여야 한다.
* - 규칙1) 벽이나 격자 판 밖으로 x
* - 규칙2) 자신이 방문한 칸으로 x
* - 규칙3) 자신의 도착 칸에 위치한 수레는 움직이지 않고 그 칸에 고정
* - 규칙4) 동시에 두 수레를 같은 칸으로 움직일 수 없음
* - 규칙5) 수레끼리 자리 바꾸며 움직일 수 x
* [목표] 필요한 최소 턴 return, 풀 수 없으면 0 return
*/
int N, M;
vvi grid;
vvi vis_blue;
vvi vis_red;
int red_i, red_j, blue_i, blue_j;
int red_end_i, red_end_j, blue_end_i, blue_end_j;
struct Node {
    int ri, rj, bi, bj;
    vector<pii> r_path, b_path;
    int depth;
    bool red_end, blue_end;
};
vector<pii> dist = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

template<typename T>
int visual_grid(const T& g){
    if (!DEBUG) return 0;
    for (int i = 0 ; i < N ; i++){
        for (int j = 0 ; j < M ; j++){
            cout << grid[i][j] << ' ';
        }
        cout << '\n';
    }
    return 0;
}

bool oob(int i, int j){
    return i < 0 || N <= i || j < 0 || M <= j;
}

int bfs(){
    deque<Node> q;
    
    q.push_back({red_i, red_j, blue_i, blue_j, {{red_i, red_j}}, {{blue_i, blue_j}}, 0, false, false});
    while (!q.empty()){
        auto [cri, crj, cbi, cbj, cr_path, cb_path, c_depth, rend, bend] = q.front(); q.pop_front();
        if (rend && bend){
            return c_depth;
        }
        vector<pii> next_red;
        for (auto [di, dj]: dist) { // red부터 움직이기
            if (rend) {
                next_red.push_back({cri, crj});
                break;
            }
            int nri = cri + di, nrj = crj + dj;
            pii next = {nri, nrj};
            if (oob(nri, nrj)) continue;
            if (grid[nri][nrj] == 5) continue;
            // if (nri == cbi && nrj == cbj) continue; => 서로 교차하는 경우만 예외로 하면 됨
            if (find(cr_path.begin(), cr_path.end(), next) != cr_path.end()) continue;
            next_red.push_back(next);
        }
        vector<pii> next_blue;
        for (auto [di, dj]: dist) { // blue
            if (bend) {
                next_blue.push_back({cbi, cbj});
                break;
            }
            int nbi = cbi + di, nbj = cbj + dj;
            pii next = {nbi, nbj};
            if (oob(nbi, nbj)) continue;
            if (grid[nbi][nbj] == 5) continue;
            // if (nri == cbi && nrj == cbj) continue; => 서로 교차하는 경우만 예외로 하면 됨
            if (find(cb_path.begin(), cb_path.end(), next) != cb_path.end()) continue;
            next_blue.push_back(next);
        }
        for (auto [nri, nrj] : next_red) {
            for (auto [nbi, nbj] : next_blue) {
                if (nri == cbi && nrj == cbj && nbi == cri && nbj == crj) continue;
                if (nri == nbi && nrj == nbj) continue;
                vector<pii> new_red_path = cr_path;
                if (!rend) new_red_path.push_back({nri, nrj});
                vector<pii> new_blue_path = cb_path;
                if (!bend) new_blue_path.push_back({nbi, nbj});
                bool next_red_end = rend, next_blue_end = bend;
                if (nri == red_end_i && nrj == red_end_j) next_red_end = true;
                if (nbi == blue_end_i && nbj == blue_end_j) next_blue_end = true;
                q.push_back({nri, nrj, nbi, nbj, new_red_path, new_blue_path, c_depth+1, next_red_end, next_blue_end});
                
            }
        }
    }
    return 0;
    
}

int solution(vector<vector<int>> maze) {
    N = maze.size(); M = maze[0].size();
    grid.resize(N, vi(M, 0));
    vis_blue.resize(N, vi(M, 0)); vis_red.resize(N, vi(M, 0));
    for (int  i=0 ; i < N ; i++){
        for (int j=0 ; j < M ; j++){
            if (maze[i][j] == 1) {
                red_i = i; red_j = j;
            } else if (maze[i][j] == 2) {
                blue_i = i; blue_j=j;
            } else if (maze[i][j] == 3) {
                red_end_i = i ; red_end_j = j;
            } else if (maze[i][j] == 4) {
                blue_end_i = i ; blue_end_j = j;
            } else if (maze[i][j] == 5) {
                grid[i][j] = 5;
            }
        }
    }
    visual_grid(grid);
    int answer = bfs();
    return answer;
}