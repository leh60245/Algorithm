import sys

DEBUG = False
try:
    sys.stdin = open("example4.txt", "r")
    DEBUG = True
    print()
except FileNotFoundError:
    pass
input = sys.stdin.readline
'''
3x3 크기 배열 A, 1초마다 배열에 연산 적용
[R] 배열 A 모든 행(row)에 대해 정렬 수행,
  단, 행 개수 >= 열 개수인 경우에 적용된다.
[C] 배열 A 모든 열(col)에 대해 정렬 수행
  단, 행 개수 < 열 개수인 경우에 적용

[조건] 한 행 또는 열에 있는 수를 정렬하려면, 
1. 각각의 수가 '몇 번' 나왔는지 알아야 한다.
2. 수의 등장 횟수가 커지는 순으로 정렬. 여러가지면 수가 커지는 순으로 정렬
3. 배열 A에 결과 저장. 이때, 수와 등장한 횟수 모두 넣으며, 순서는 수가 먼저.

정렬된 결과를 배열에 다시 넣으면 행 또는 열 크기 달라짐
R 연산이 적용된 경우 -> 가장 큰 행을 기준으로 모든 행의 크기가 변화
C 연산이 적용된 경우 -> 가장 큰 열의 기준으로 모든 열의 크기가 변화
행 또는 열의 크기가 커진 곳에 0 채워짐
수를 정렬할 때 0은 무시. 
Ex) [3, 2, 0, 0] 정렬 결과 == [3, 2] 정렬 결과와 동일.

[IF] 행 또는 열 크기가 100 넘어가는 경우 
  ->  처음 100개를 제외한 나머지는 버림
[목표] A[r][c]에 들어있는 값이 k가 되기 위한 최소 시간 구하기.
    만약 100초가 지나도 k가 되지 않으면 -1 출력
'''
R, C, K = map(int, input().split())
R, C = R - 1, C - 1
grid = list()
for _ in range(3):
    grid.append(list(map(int, input().split())))


def mirror(grid):
    n, m = len(grid), len(grid[0])
    new_grid = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_grid[j][i] = grid[i][j]
    return new_grid


def visualize(g, time):
    print(f"====== visual-{time} ======")
    for l in g:
        print(*l)


def main():
    global grid
    time = 0
    while True:
        if R < len(grid) and C < len(grid[0]) and grid[R][C] == K:
            print(time)
            return
        if time >= 100:
            print(-1)
            return

        N, M = len(grid), len(grid[0])
        base_grid, is_mirror = (grid.copy(), False) if N >= M else (mirror(grid), True)

        new_grid = []
        max_len = 0
        for line in base_grid:
            v_to_idx = {}
            cnt_value = list()
            idx = 0
            for v in line:
                if v == 0:
                    continue
                if v not in v_to_idx.keys():
                    v_to_idx[v] = idx
                    cnt_value.append((v, 1))
                    idx += 1
                else:
                    tmp = v_to_idx[v]
                    v, cnt = cnt_value[tmp]
                    cnt_value[tmp] = (v, cnt + 1)

            cnt_value.sort(key=lambda x: (x[1], x[0]))
            new_line = list()
            for v, c in cnt_value:
                new_line.append(v)
                new_line.append(c)

            max_len = max(max_len, len(new_line))
            new_grid.append(new_line)

        max_len = min(max_len, 100)
        for i in range(len(new_grid)):
            l = len(new_grid[i])
            if l > 100:
                new_grid[i] = new_grid[i][:100]
            else:
                new_grid[i] = new_grid[i] + [0] * (max_len - l)

        if not is_mirror:
            grid = new_grid
        else:
            grid = mirror(new_grid)

        time += 1
        if DEBUG:
            visualize(grid, time)
            print(f"max len = {max_len}")

if __name__ == "__main__":
    main()
