import sys
from collections import deque
from itertools import combinations

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

input = sys.stdin.readline
grid = [input().strip() for _ in range(5)]
grid_arr = [(i, j) for i in range(5) for j in range(5)]


def is_connected(group):
    q = deque()
    v = set()
    cnt = 0

    q.append(group[0])
    v.add(group[0])
    cnt += 1

    while q:
        i, j = q.popleft()
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if (ni, nj) not in group or (ni, nj) in v:
                continue
            v.add((ni, nj))
            q.append((ni ,nj))
            cnt += 1

    return cnt == 7

def main():
    answer = 0
    for group in combinations(grid_arr, 7):
        if sum(1 for i, j in group if grid[i][j] == 'S') >= 4:
            if is_connected(group):
                answer += 1
    print(answer)


if __name__ == "__main__":
    main()
