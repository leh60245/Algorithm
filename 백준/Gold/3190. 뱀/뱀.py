import sys
from collections import deque

try:
    sys.stdin = open("example1.txt", "r")
except FileNotFoundError:
    pass
input = sys.stdin.readline
N = int(input())
K = int(input())
apple = set()
for _ in range(K):
    ax, ay = map(int, input().split())
    ax, ay = ax - 1 , ay - 1
    apple.add((ax, ay))
L = int(input())
head_cmd = dict()
for _ in range(L):
    t, h = map(str, input().split())
    t = int(t)
    if h == 'L':
        head_cmd[t] = -1
    else:
        head_cmd[t] = 1
dd = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동 남 서 북


def oob(i, j):
    return not (0 <= i < N and 0 <= j < N)


def main():
    body = deque()  # tail ~ head
    head_dir = 0

    body.append((0, 0))
    all_time = 0
    while True:
        all_time += 1
        hi, hj = body[-1]
        di, dj = dd[head_dir]
        ni, nj = hi + di, hj + dj  # 머리를 늘린다.
        if oob(ni, nj) or (ni, nj) in body:
            print(all_time)
            return
        if (ni, nj) in apple:  # 사과 발견
            apple.remove((ni, nj))
            body.append((ni, nj))
        else:
            body.append((ni, nj))
            body.popleft()

        if all_time in head_cmd:
            head_dir = (head_dir + head_cmd[all_time]) % 4



if __name__ == "__main__":
    main()
