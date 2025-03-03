import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

input = sys.stdin.readline
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [0 for _ in range(N)]
result = [0 for _ in range(M)]


def backtracking(cnt):
    if cnt == M:
        print(*result)
        return
    tmp = -1
    for i in range(N):
        if not visited[i] and arr[i] != tmp:
            visited[i] = 1
            tmp = arr[i]
            result[cnt] = arr[i]
            backtracking(cnt + 1)
            visited[i] = 0


def main():
    backtracking(0)


if __name__ == "__main__":
    main()
