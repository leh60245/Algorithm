import sys
from collections import deque

DEBUG = False
try:
    sys.stdin = open("example4.txt", "r")
    DEBUG = True
    print()
except FileNotFoundError:
    pass
input = sys.stdin.readline
'''
NxN 크기 공간, 물고기 M, 아기 상어 1마리, 한 칸에 물고리 최대 1마리 존재
아기 상어와 물고기 모두 크기 가짐
  초기 아기 상어 크기 = 2
  아기 상어는 1초에 상하좌우로 한 칸씩 이동
  [조건] 자기 크기보다 큰 물고기 칸은 지날 수 없다.
  [조건] 자신 크기보다 작은 물고기만 먹을 수 없다.
  [조건] 크기가 같은 물고기는 먹을 수 없지만, 지날 수 있다.

이동 결정 방법
1. [종료] 더 이상 먹을 수 있는 물고기가 없다면
  -> 엄마에게 도움 요청
2. 먹을 수 있는 물고기가 1마리라면,
  -> 그 물고기를 먹는다.
3. 먹을 수 있는 물고기가 1마리보다 크면
  -> 거리가 가장 가까운 물고기를 먹는다.
      거리 = 아기상어 ~ 물고기 유클리드 거리
      거리가 가까운 물고기가 많다면
          -> 가장 위 물고기 (i 최소), 그 다음 가장 왼쪽 물고기 (j 최소)

아기 상어 이동에 1초 걸림, 물고기 먹는데 걸리는 시간은 없다.
물고기를 먹으면, 그 칸은 빈 칸이 됨
자신의 크기와 같은 수의 물고리르 먹을 때마다 크기가 1 증가

[목표] 몇 초 동안, 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하자.
'''
N = int(input())
fish = [[0 for _ in range(N)] for _ in range(N)]
shark = (None, None, None, None)  # i, j, size, eating
for i in range(N):
    for j, v in enumerate(list(map(int, input().split()))):
        if 1 <= v <= 6:
            fish[i][j] = v
        elif v == 9:
            shark = (i, j, 2, 0)


def bfs(s):
    si, sj, s_size, s_eating = s
    global fish
    q = deque([])
    visited = [[0 for _ in range(N)] for _ in range(N)]  # 걸리는 시간도 표시
    min_distant = float('inf')
    can_eat_fish = list()

    q.append((si, sj))
    visited[si][sj] = 1  # 초기가 1이라 나중에 1 빼줘야 함.
    while q:
        ci, cj = q.popleft()
        if 0 < fish[ci][cj] < s_size:   # 물고기 수집하기
            dist = visited[ci][cj] - 1
            if dist < min_distant:
                min_distant = dist
                can_eat_fish = list()  # 더 가까운 물고기를 찾았으니, 초기화
                can_eat_fish.append((ci, cj))
            elif dist == min_distant:
                can_eat_fish.append((ci, cj))

        for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < N and 0 <= nj < N) or visited[ni][nj] or fish[ni][nj] > s_size:
                continue
            q.append((ni, nj))
            visited[ni][nj] = visited[ci][cj] + 1

    if not can_eat_fish:
        return (si, sj, s_size, s_eating), 0 # 못 먹음

    can_eat_fish.sort()
    fi, fj = can_eat_fish[0]
    fish[fi][fj] = 0
    if s_size == (s_eating + 1):
        return (fi, fj, s_size+1, 0), min_distant
    else:   # s_size > s_eating
        return (fi, fj, s_size, s_eating+1), min_distant


vcnt = 0
def visual(time, times):
    global vcnt
    print(f"=========== visual-{vcnt} ===========")

    si, sj, _, _ = shark
    for i in range(N):
        for j in range(N):
            if (i, j) == (si, sj):
                print("9", end=" ")
            else:
                print(fish[i][j], end=" ")
        print()
    print(f"time: {time}, all time: {times}")
    print(f"shark info: {shark}")
    vcnt += 1


def main():
    global shark
    time = 0
    times = 0
    while True:
        if DEBUG:
            visual(time, times)
        shark, time = bfs(shark)

        if not time:
            break

        times += time


    print(times)


if __name__ == "__main__":
    main()
