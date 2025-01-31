N, M = map(int, input().split())
visited = [0] * (N+1)

def backtracking(n, arr):
    if len(arr) == M:
        print(*arr)
        return
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            backtracking(n, arr+[i])
            visited[i] = 0

backtracking(N, [])