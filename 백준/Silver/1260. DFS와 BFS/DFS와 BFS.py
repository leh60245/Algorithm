import sys
from collections import deque

try:
    sys.stdin = open("example3.txt", "r")
except FileNotFoundError:
    pass

input = sys.stdin.readline
N, M, V = map(int, input().split())
grid = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    grid[i][j] = 1
    grid[j][i] = 1
dfs_path = []

def dfs(start_node, visited):
    visited[start_node] = 1
    dfs_path.append(start_node)
    for neighbor_node, is_next in enumerate(grid[start_node]):
        if is_next and not visited[neighbor_node]:
            dfs(neighbor_node, visited)

def bfs(si):
    q = deque()
    v = []

    q.append(si)
    v.append(si)
    while q:
        row = q.popleft()
        for col in range(N + 1):
            if grid[row][col] and col not in v:
                q.append(col)
                v.append(col)
    return v


def main():
    dfs(V, [0 for _ in range(N + 1)])
    print(*dfs_path)
    print(*bfs(V))


if __name__ == "__main__":
    main()
