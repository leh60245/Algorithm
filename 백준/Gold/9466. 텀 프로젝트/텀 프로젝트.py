import sys
from collections import deque
from itertools import cycle

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

input = sys.stdin.readline


def bfs(si, arr, visited):
    q = deque()
    path = []

    q.append(si)
    visited[si] = 1
    path.append(si)
    while q:
        ci = q.popleft()
        ni = arr[ci]
        if visited[ni]:
            if ni in path:
                cycle_start = path.index(ni)
                return cycle_start
            return len(path)
        else:  # not v[ni]
            visited[ni] = 1
            q.append(ni)
            path.append(ni)
    return len(path)


def main():
    T = int(input())
    for _ in range(T):
        answer = 0
        n = int(input())
        arr = list(map(lambda x: int(x) - 1, input().split()))
        visited = [0] * n
        for i in range(n):
            if not visited[i]:
                answer += bfs(i, arr, visited)
        print(answer)


if __name__ == "__main__":
    main()
