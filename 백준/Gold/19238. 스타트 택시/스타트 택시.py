import sys
from collections import deque

DEBUG = False
# try:
#     sys.stdin = open("example.txt", "r")
#     DEBUG = True
#     print()
# except FileNotFoundError:
#     pass
input = sys.stdin.readline


def visual_print(time):
    if not DEBUG: return
    print("=" * 10, "time:", time, "=" * 10)
    return


def visual_grid(grid, car, point=None):
    if not DEBUG: return
    tmp = [l[:] for l in grid]
    if point is not None:
        for pi, pj in point:
            tmp[pi][pj] = "●"
    for i in range(len(grid)):
        for j in range(len(grid)):
            if (i, j) == car:
                print("★", end=" ")
            else:
                print(tmp[i][j], end=" ")
        print()
    print()
    return


def move_to_people(car, people, grid, gas, n):
    q = deque()
    v = [[-1] * n for _ in range(n)]
    new_grid = [[-1] * n for _ in range(n)]
    for p_idx, p in enumerate(people):
        new_grid[p[0]][p[1]] = p_idx
    dist = gas
    can_take_people = list()

    q.append(car)
    v[car[0]][car[1]] = 0
    while q:
        ci, cj = q.popleft()
        if v[ci][cj] > dist:
            # 최소 거리보다 멀리 왔다면 마무리
            continue
        if new_grid[ci][cj] >= 0:
            if v[ci][cj] < dist:
                dist = v[ci][cj]
                can_take_people = [(ci, cj)]
            elif v[ci][cj] == dist:
                can_take_people.append((ci, cj))
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < n and 0 <= nj < n) or v[ni][nj] >= 0 or grid[ni][nj]: continue
            q.append((ni, nj))
            v[ni][nj] = v[ci][cj] + 1

    if not can_take_people:
        return (-1, -1), -1

    can_take_people.sort(key=lambda x: (x[0], x[1]))
    pi, pj = can_take_people[0]
    return (pi, pj), gas - dist


def move_to_destination(car, arrive, grid, gas, n):
    q = deque()
    v = [[-1] * n for _ in range(n)]

    q.append(car)
    v[car[0]][car[1]] = 0

    while q:
        ci, cj = q.popleft()
        if v[ci][cj] > gas:
            continue
        if (ci, cj) == arrive:
            return arrive, gas + v[ci][cj]

        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < n and 0 <= nj < n) or v[ni][nj] >= 0 or grid[ni][nj]: continue
            q.append((ni, nj))
            v[ni][nj] = v[ci][cj] + 1

    return (-1, -1), -1


def solve(n, m, gas, grid, car, people, arrive):
    time = 1
    while True:
        if len(people) == 0:
            return gas
        visual_print(time)
        visual_grid(grid, car)
        # [1] 사람 구하기
        # 차가 사람까지 가서 도착하면 다음 차 위치와 남은 가스 반환
        # 남은 가스가 0 이하라면 끝
        car, gas = move_to_people(car, people, grid, gas, n)
        if gas <= 0:
            break
        visual_grid(grid, car, people)

        # [2] 도착 하기
        # 차가 사람을 태우고 도착하면 다음 차 위치와 남은 가스 반환
        # 남은 가스가 0 이하라면 끝
        arrive_index = people.index(car)
        car, gas = move_to_destination(car, arrive[arrive_index], grid, gas, n)
        if gas <= 0:
            break
        visual_grid(grid, car, arrive)

        # [3] 출발지와 도착지 지우기
        del people[arrive_index]
        del arrive[arrive_index]
        time += 1

    return -1


def main():
    N, M, gas = map(int, input().split())  # 격자 크기, 사람 수, 초기 가스
    grid = [list(map(int, input().split())) for _ in range(N)]
    ci, cj = map(int, input().split())  # 초기 차 위치
    car = (ci - 1, cj - 1)
    people_start = list()
    people_end = list()
    for _ in range(M):
        si, sj, ei, ej = map(int, input().split())  # 출발지&목적지
        si, sj, ei, ej = si - 1, sj - 1, ei - 1, ej - 1
        people_start.append((si, sj))
        people_end.append((ei, ej))

    result = solve(N, M, gas, grid, car, people_start, people_end)
    print(result)
    return 0


if __name__ == "__main__":
    main()
