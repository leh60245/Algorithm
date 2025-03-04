import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

input = sys.stdin.readline
result = [0 for _ in range(6)]
visited = list()


def backtracking(l, s, cnt):
    if cnt == 6:
        print(*result)
        return
    for i in range(l):
        if visited[i]:
            continue
        if cnt > 0 and s[i] < result[cnt-1]:
            continue
        visited[i] = 1
        result[cnt] = s[i]
        backtracking(l, s, cnt + 1)
        visited[i] = 0


def main():
    global visited
    while True:
        cmd = list(map(int, input().split()))
        if 0 in cmd:
            break
        lenght, S = cmd[0], cmd[1:]
        visited = [0 for _ in range(lenght)]
        backtracking(lenght, S, 0)
        print()


if __name__ == "__main__":
    main()
