N = int(input())
arr = list(map(int, input().split()))

stack = [(100000001, 0)]
answer = []


for i in range(N):
    while stack != [] and stack[-1][0] < arr[i]:
        stack.pop()

    answer.append(stack[-1][1])
    stack.append((arr[i], i+1))


print(*answer)