import sys

# from collections import deque

DEBUG = False
try:
    sys.stdin = open("example4.txt", "r")
    DEBUG = True
    print()
except FileNotFoundError:
    pass
input = sys.stdin.readline
'''
NxN 격자, N은 항상 홀수, 상어는 언제나 N//2, N//2
각 칸에 번호는 상어부터 좌에서 시작해 회오리로 번호 붙여짐
상어부터 좌 하 우 상 이렇게 움직임

상어칸 제외하고 구슬 1~3번이 각 칸에 있다. 
같은 번호 가진 구슬이 번호가 연속하는 칸이 있으면, 그 구슬을 <연속하는 구슬>이라고 한다.

[1. 마법 시전]
1. 방향 di와 거리 si를 정해야 한다.
    - 방향 상 하 좌 우 각각 1 2 3 4
2. 상어는 di 방향으로 거리 si 이하인 모든 칸에 구슬 모두 파괴
3. 구슬 파괴되면 구슬이 들어있지 않은 빈 칸이 된다.
    - 벽은 파괴되지 않는다.

[2. 구슬 이동]
만약 어떤 칸 A의 번호보다 번호가 하나 작은 칸이 빈 칸이면, A에 있는 구슬이 빈칸으로 이동
더 이상 구슬이 이동하지 않을 때까지 반복한다.

[3. 구슬 폭파] <<<<여기서 폭발한 구슬의 개수를 얻는다.>>>>
4개 이상 연속하는 구실이 있을때 발생.
구슬이 폭발해 빈 칸이 생기면 다시 [구슬 이동]이 생긴다.
더 이상 폭발하는 구슬이 없을 때까지 반복된다.
    

[4. 구슬 변화]
연속하는 구슬은 하나의 그룹이라고 한다.
<하나의 그룹>은 <두 개의 구슬 A와 B>로 변한다.
- 구슬 A의 번호는 = 그룹에 들어 있는 '구슬의 <개수>'
- 구슬 B의 번호는 = 그룹을 이루고 있는 '구슬의 <번호>'
구슬은 다시 그룹의 순서대로 1번 칸부터 차례대로 A, B 순서로 칸에 들어간다.
만약, 구슬이 칸의 수보다 많아 칸에 들어가지 못하는 경우, 그러한 구슬은 사라진다.

[목표]
1×(폭발한 1번 구슬의 개수) + 2×(폭발한 2번 구슬의 개수) + 3×(폭발한 3번 구슬의 개수)

[조건] 마법 총 M번 시전
3 ≤ N ≤ 49
N은 홀수
1 ≤ M ≤ 100
1 ≤ di ≤ 4
1 ≤ si ≤ (N-1)/2
칸에 들어있는 구슬이 K개라면, 구슬이 들어있는 칸의 번호는 1번부터 K번까지이다.
입력으로 주어진 격자에는 4개 이상 연속하는 구슬이 없다.
'''
N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
cmd_list = list()
for _ in range(M):
    dddd, sssss = map(int, input().split())
    cmd_list.append((dddd - 1, sssss))
DIRECTION = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dprint(*args, **kwargs):
    if not DEBUG:
        return
    print(*args, **kwargs)


def visualize_grid(p, b):
    if not DEBUG:
        return
    sub_grid = [[0] * N for _ in range(N)]
    for bi, v in enumerate(b):
        i, j = p[bi]
        sub_grid[i][j] = v
    for i in range(N):
        for j in range(N):
            if sub_grid[i][j] == 0:
                print("■", end=" ")
            else:
                print(sub_grid[i][j], end=" ")
        print()


def storm():
    path = list()
    ball = list()
    sub_grid = [[0] * N for _ in range(N)]
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    si, sj, sd = 0, 0, 0

    path.append((si, sj))
    if grid[si][sj]:
        ball.append(grid[si][sj])
    sub_grid[si][sj] = 1
    for n in range(1, N * N - 1):
        di, dj = direction[sd]
        ni, nj = si + di, sj + dj
        if not (0 <= ni < N and 0 <= nj < N) or sub_grid[ni][nj] > 0:
            sd = (sd + 1) % 4
            di, dj = direction[sd]
            ni, nj = si + di, sj + dj
        path.append((ni, nj))
        if grid[ni][nj] >= 1:
            ball.append(grid[ni][nj])
        sub_grid[ni][nj] = n + 1
        si, sj = ni, nj

    path.reverse()
    ball.reverse()
    return path, ball


def blizzard(path, ball, cmd):
    n = len(path)
    d, size = cmd
    di, dj = DIRECTION[d]
    si, sj = N // 2, N // 2
    sp = n - 1
    for s in range(size, 0, -1):
        ni, nj = si + di * s, sj + dj * s
        for p_idx in range(sp, -1, -1):
            if (ni, nj) == path[p_idx]:
                if p_idx < len(ball):
                    ball.pop(p_idx)
                sp = p_idx - 1
                break
    return ball


def mv_ball(path, ball):
    pass


def bm_ball(path, ball):
    num = 0
    tmp_list = list()
    bm_list = list()
    for idx, b_n in enumerate(ball):
        if b_n != num:
            num = b_n
            if len(tmp_list) >= 4:
                bm_list = bm_list + tmp_list
            tmp_list = [idx]
        else:
            tmp_list.append(idx)
    
    if len(tmp_list) >= 4:
        bm_list = bm_list + tmp_list
    
    cnt_boom_list = [0, 0, 0]
    for i, v in enumerate(bm_list):
        cnt_boom_list[ball[v - i] - 1] += 1
        ball.pop(v - i)
    return ball, cnt_boom_list


def ts_ball(path, ball):
    n = len(ball)
    new_ball = list()
    A = 0  # 구슬 개수
    B = 0  # 구슬 번호

    A += 1
    B = ball[0]
    for idx in range(1, n):
        b_n = ball[idx]
        if b_n == B:
            A += 1
        else:
            new_ball.append(A)
            new_ball.append(B)
            A = 1
            B = b_n

    new_ball.append(A)
    new_ball.append(B)

    if len(new_ball) > N*N-1:
        return new_ball[:N*N-1]
    return new_ball

def main():
    dprint("======= storm !!! ========")
    path, ball = storm()
    visualize_grid(path, ball)
    boom_ball = [0, 0, 0]
    t = 1
    for cmd in cmd_list:
        dprint(f"========= time {t} ===========")
        dprint("command:", cmd)
        # 1. 마법 시전
        dprint("<<<< blizzard!!! >>>>")
        ball = blizzard(path, ball, cmd)
        visualize_grid(path, ball)

        # 2&3. 구슬 이동 & 구슬 폭파
        dprint("<<<< BOOM!!! >>>>")
        while True:
            # ball = mv_ball(path, ball)
            ball, cnt_boom_ball = bm_ball(path, ball)
            visualize_grid(path, ball)
            dprint("how many ball is boom:", cnt_boom_ball)
            if sum(cnt_boom_ball) == 0:
                dprint("no boom")
                break
            for i, v in enumerate(cnt_boom_ball):
                boom_ball[i] += v

        if len(ball) == 0:
            break

        # 4. 구슬 변화
        dprint("<<<< transform!!! >>>>")
        ball = ts_ball(path, ball)
        visualize_grid(path, ball)
        dprint("\n\n")
        t += 1

    # 점수 계산
    score = 0
    for i, v in enumerate(boom_ball):
        score += (i + 1) * v
    print(score)


if __name__ == "__main__":
    main()
