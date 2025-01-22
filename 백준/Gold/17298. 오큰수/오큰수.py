N = int(input())
arr = list(map(int, input().split()))

stack = []
answer = [-1] * N

for i in range(N):
    while stack and stack[-1][0] < arr[i]:
        _, idx = stack.pop()
        answer[idx] = arr[i]
    stack.append((arr[i], i))


print(*answer)