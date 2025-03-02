import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

input = sys.stdin.readline
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = [0 for _ in range(M)]
visited = [False for _ in range(N)]


def backtracking(cnt):
    if cnt == M:
        print(*result)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result[cnt] = arr[i]
            backtracking(cnt+1)
            visited[i] = False


def main():
    backtracking(0)


if __name__ == "__main__":
    main()
