import sys
from collections import deque

input = sys.stdin.readline
N, L, R = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))


# 국경선 공유하는 두 나라 인구 차이가 L <= ? <= R 라면 국경선을 하루 동안 연다
#   위 조건으로 국경선이 모두 열렸다면, 인구 이동을 시작한다.
# 국경선이 열려 있는 각 나라는 연합이다.
# 연합을 이루는 각 칸의 인구수는 sum_people // num_block 이다.
# 연합을 해체하고, 모든 국경선을 닫는다.
# answer: 인구 이동이 며칠 동안 발생하는가?

def in_box(i, j):
    return 0 <= i < N and 0 <= j < N


def bfs(si, sj):
    # [1] 생성
    global arr
    q = deque()
    global v
    save_points = []
    sum_people, num_blocks = 0, 0

    # [2] 초기 설정
    q.append((si, sj))
    v[si][sj] = 1
    save_points.append((si, sj))
    sum_people, num_blocks = arr[si][sj], 1

    # [3]
    while q:
        ci, cj = q.popleft()
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = ci + di, cj + dj
            if in_box(ni, nj) and not v[ni][nj] and L <= abs(arr[ci][cj] - arr[ni][nj]) <= R:
                q.append((ni, nj))
                v[ni][nj] = 1
                save_points.append((ni, nj))
                sum_people += arr[ni][nj]
                num_blocks += 1

    for i, j in save_points:
        arr[i][j] = sum_people // num_blocks

    if num_blocks > 1:
        return 1
    else:
        return 0


ans = 0
while True:
    v = [[0] * N for _ in range(N)]
    is_move = 0
    for i in range(N):
        for j in range(N):
            if not v[i][j]:
                is_move += bfs(i, j)

        # 더 이상 변화가 없다면 끝 -> 인구에 변화가 있냐 없냐는 어떻게 알아낼 수 있을까? 국경선이 열리면 해결?
    if not is_move:
        break
    ans += 1

print(ans)
