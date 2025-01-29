import sys
from collections import deque

input = sys.stdin.readline

dist = [(1, 2), (-1, 2), (1, -2), (-1, -2),
        (2, 1), (-2, 1), (2, -1), (-2, -1),]

def inBox(i, j, N, M):
    return 0 <= i < N and 0 <= j < M

T = int(input())
for _ in range(T):
    I = int(input())
    SI, SJ = map(int, input().split())
    AI, AJ = map(int, input().split())

    def beq(si, sj):
        q = deque()
        visited = [[0 for _ in range(I)] for _ in range(I)]

        q.append((si, sj))
        visited[si][sj] = 1
        while q:
            ci, cj = q.popleft()
            if (ci, cj) == (AI, AJ):
                return visited[ci][cj] - 1
            for di, dj in dist:
                ni, nj = ci + di, cj + dj
                if not inBox(ni, nj, I, I) or visited[ni][nj]:
                    continue
                visited[ni][nj] = visited[ci][cj] + 1
                q.append((ni, nj))

        return 0

    print(beq(SI, SJ))