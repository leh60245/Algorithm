import sys
from collections import deque

DEBUG = False
try:
    sys.stdin = open("example3.txt", "r")
    DEBUG = True
    print()
except FileNotFoundError:
    pass
input = sys.stdin.readline
'''
NxN 격자. 초기 격자 모든 칸에는 블록이 하나씩 있고, 
블록 종류: 검은색(-1), 무지개(0), 일반
일반 블록 색상 M가지. 색은 M 이하의 자연수로 표현된다.
인접한 블록은 상하좌우

[블록 그룹 조건] 블록 그룹은 연결된 블록의 집합. 
1. 그룹에는 일반 블록이 적어도 하나 있어야 하고, 일반 블록의 색은 모두 동일
2. 검은 블록은 포함되면 안되고, 무지개 블록은 얼마나 들어 있어도 상관 없음
3. 그룹에 속한 블록 개수는 2보다 크거나 같아야 한다.
4. 그룹에 속한 블록은 모두 연결되어 있다.
5. <기준 블록> 블록 그룹의 기준 블록은 무지개 블록 X, 행과 열의 번호가 가장 작은 블록이다.

[오토 플레이] 
[종료 조건] 블록 그룹이 존재하는 동안 계속 반복
1. 크기가 가장 큰 블록 그룹을 찾는다.
    - 그러한 블록이 여러개라면 -> 포함된 <무지개 블록 수>가 가장 많은 블록 그룹,
    - 그러한 블록이 여러개라면 -> 기준 블록의 <행>이 가장 큰 것, 그 다음은 <열>이 큰 것
2. [point 획득] 1에서 찾은 블록 그룹의 모든 블록을 제거한다. 
    - 블록 그룹에 포함된 블록 수를 B라 했을 때, B**2 점을 획득한다.
3. 격자에 중력이 작용한다.
4. 격자가 90도 반시계 방향으로 회전한다.
5. 다시 격자에 중력이 작용한다.
[중력 작용] 중력이 있을 때, 
- 검은 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동
- 이동은 다른 블록이나 격자의 경계를 만나기 전까지 계속된다. 
'''
BLANK, BLACK, RAINBOW = -2, -1, 0
N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))


def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


def visualize_grid():
    if not DEBUG:
        return
    for line in grid:
        for v in line:
            if v == BLANK:
                print("□", end=" ")
            elif v == BLACK:
                print("■", end=" ")
            elif v == RAINBOW:
                print("◎", end=" ")
            else:
                print(v, end=" ")
        print()
    print()


def visualize_group_grid(g_b, num):
    if not DEBUG:
        return
    for i in range(N):
        for n in range(1, num+1):
            for j in range(N):
                if (i, j) in g_b[n]:
                    print(n, end=" ")
                else:
                    print(0, end=" ")
            print(" || ", end=" ")
        print()

    return


def bfs(si, sj, num, visited):
    q = deque([])
    v_rainbow = list()
    path = []
    color = grid[si][sj]

    q.append((si, sj))
    visited[si][sj] = 1
    path.append((si, sj))

    while q:
        ci, cj = q.popleft()

        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < N and 0 <= nj < N) or grid[ni][nj] <= BLACK or visited[ni][nj]:
                continue
            if grid[ni][nj] == 0:  # rainbow
                q.append((ni, nj))
                visited[ni][nj] = 1
                v_rainbow.append((ni, nj))
                path.append((ni, nj))

            elif grid[ni][nj] == color:  # 동일한 색
                q.append((ni, nj))
                visited[ni][nj] = 1
                path.append((ni, nj))

    # rainbow 블록은 방문 기록에서 제거
    for ri, rj in v_rainbow:
        visited[ri][rj] = 0

    # 기준 블록
    path.sort()
    bi, bj = None, None
    for pi, pj in path:
        if grid[pi][pj] > RAINBOW:
            bi, bj = pi, pj
            break
    size = len(path)
    r_cnt = len(v_rainbow)
    return path, (size, r_cnt, bi, bj), visited


def clean_blocks(path):
    global grid
    for i, j in path:
        grid[i][j] = BLANK


def gravity():
    global grid
    for col in range(N):
        for row in range(N - 2, -1, -1):
            if grid[row][col] >= RAINBOW:
                nr = row
                while nr < N - 1 and grid[nr + 1][col] == BLANK:
                    grid[nr + 1][col] = grid[nr][col]
                    grid[nr][col] = BLANK
                    nr += 1


def rotate_anticlockwise():
    global grid
    new_grid = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_grid[N - j - 1][i] = grid[i][j]
    grid = new_grid


def main():
    cnt = 1
    points = 0
    while True:
        dprint(f"====== {cnt}번 과정 전개 ========")
        # 1. 블록 그룹 찾기

        # 그룹 정보: (size, rainbow, base_i, base_j) => 모두 크기 순으로 나열만 하면 됨.
        group_blocks = {}  # { 그룹 넘버: [블록 위치, ...], 그룹 넘버: [블록 위치, ...], ... }
        info_list = list()  # [ (그룹 정보), (그룹 정보), ... ]
        info_to_number = {}  # { (그룹 정보): 그룹 넘버, (그룹 정보): 넘버, ... }
        visited = [[0] * N for _ in range(N)]
        g_num = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j] > 0 and not visited[i][j]:
                    path, info, new_visited = bfs(i, j, g_num, visited)
                    if len(path) < 2:
                        continue
                    g_num += 1
                    visited = new_visited
                    group_blocks[g_num] = path
                    info_list.append(info)
                    info_to_number[info] = g_num
        if len(info_list) == 0:
            break

        info_list.sort()
        largest_group_info = info_list[-1]
        largest_group_number = info_to_number[largest_group_info]
        largest_group_blocks = group_blocks[largest_group_number]

        dprint(f"나열된 그룹 {len(info_list)}개")
        dprint(f">> 가장 큰 그룹 {largest_group_number}: ", largest_group_info)
        visualize_group_grid(group_blocks, len(info_list))

        # 2. 블록 지우고 point 얻기
        clean_blocks(largest_group_blocks)
        points += len(largest_group_blocks) ** 2

        dprint(f"점수 얻기 {len(largest_group_blocks) ** 2}, 누적 {points}")
        visualize_grid()

        # 3. 중력 작용
        gravity()
        dprint("첫 번째 중력 작용")
        visualize_grid()

        # 4. 격자 반시계 90도 회전
        rotate_anticlockwise()
        dprint("회전")
        visualize_grid()

        # 5. 중력 작용
        gravity()
        dprint("두 번째 중력 작용")
        visualize_grid()

        dprint("")
        cnt += 1
    print(points)


if __name__ == "__main__":
    main()
