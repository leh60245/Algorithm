import sys
from collections import deque

try:
    sys.stdin = open("example2.txt", "r")
except FileNotFoundError:
    pass
input = sys.stdin.readline
# 직사각형 보드, 빨간 구슬 1개, 파란 구슬 1개
# ending: 빨간 구슬을 구멍에 위치

# N*M, 가장 바같 행과 열은 모두 벽, 구멍은 1개
# 빨간, 파랑 각각 1개
# 목표: 빨간 구슬을 구멍으로. 단, 파란 구슬은 들어가면 안된다.

# 4방향 기울기로 구슬 옮기기
# 구슬은 동시에 움직임.
# success: 빨간 구슬 만 구멍에
# fail: 파란 구슬이 나감 (빨간 구슬이 구멍에 도착해도, 파란 구슬이 도착할 수 있는 것을 주의하자)
# 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다.
# 모두 1x1 크기
# 기울기 동작을 멈추는 것은 더 이상 구슬이 움직이지 않을때 까지.

# print: 최소 몇 번 만에 구슬이 구멍을 통해 빼낼 수 있는지 구하기
# 단, 10번 이하로 움직여 빨간 구슬을 구멍으로 빼낼 수 없으면 -1 출력

N, M = map(int, input().split())
grid = list()
walls = set()
hole = tuple()
ri, rj = None, None
bi, bj = None, None

for i in range(N):
    temp = input().strip()
    for j, entry in enumerate(temp):
        if entry == '#':
            walls.add((i, j))
        elif entry == 'O':
            hole = (i, j)
        elif entry == 'R':
            ri, rj = i, j
        elif entry == 'B':
            bi, bj = i, j
        else:
            pass
dd = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 공의 이동 방향 - 동 남 서 북


def move_ball(i, j, oi, oj, sd):
    ci, cj = i, j
    di, dj = dd[sd]
    while True:
        ni, nj = ci + di, cj + dj
        if (ni, nj) == hole:
            return ni, nj
        if (ni, nj) in walls or (ni, nj) == (oi, oj):
            return ci, cj
        ci, cj = ni, nj


def bfs(ri, rj, bi, bj):
    q = deque()
    visited = set()

    q.append((ri, rj, bi, bj, 0))
    visited.add((ri, rj, bi, bj))
    while q:
        cri, crj, cbi, cbj, cdepth = q.popleft()
        if cdepth >= 10:
            return -1
        for i in range(4):
            if ((i == 0 and cbj < crj) or
                    (i == 1 and cbi < cri) or
                    (i == 2 and cbj > crj) or
                    (i == 3 and cbi > cri)):
                nri, nrj = move_ball(cri, crj, cbi, cbj, i)
                nbi, nbj = move_ball(cbi, cbj, nri, nrj, i)
            else:
                nbi, nbj = move_ball(cbi, cbj, cri, crj, i)
                nri, nrj = move_ball(cri, crj, nbi, nbj, i)

            if (nbi, nbj) == hole:
                continue
            if (nri, nrj) == hole:
                return cdepth + 1

            if (nri, nrj, nbi, nbj) not in visited:
                visited.add((nri, nrj, nbi, nbj))
                q.append((nri, nrj, nbi, nbj, cdepth + 1))
    return -1

def main():
    print(bfs(ri, rj, bi, bj))


if __name__ == "__main__":
    main()
