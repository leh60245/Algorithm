import sys
from collections import deque

input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())


# F: 총 층 수
# S: 현 위치
# G: 도착지
# U: U층 위
# D: D층 아래

def in_floar(i):
    return 1 <= i <= F


def dfs(s):
    # [1] 초기 설정
    q = deque()
    v = [0] * (F + 1)

    # [2] 값 입력
    q.append(s)
    v[s] = 1

    # 위치
    while q:
        now_floar = q.popleft()
        if now_floar == G:
            return v[now_floar] - 1
        for move in [U, D * (-1)]:
            next_floar = now_floar + move
            if in_floar(next_floar) and not v[next_floar]:
                v[next_floar] = v[now_floar] + 1
                q.append(next_floar)

    return "use the stairs"


ans = dfs(S)
print(ans)
