import sys
from collections import deque

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

input = sys.stdin.readline
N, K = map(int, input().split())


def bfs(si):
    q = deque()
    visited = [0 for _ in range(100001)]

    q.append(si)
    visited[si] = 1
    while q:
        ci = q.popleft()
        if ci == K:
            return visited[ci] - 1
        for di in [ci, 1, -1]:
            ni = ci + di
            if not (0 <= ni < 100001) or visited[ni]:
                continue
            q.append(ni)
            visited[ni] = visited[ci] + 1

    return -1


def main():
    print(bfs(N))


if __name__ == "__main__":
    main()
