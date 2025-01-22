N = int(input())
stack = []
answer = 0

for i in range(1,N+1):
    height = int(input())
    while stack and stack[-1] <= height:
        stack.pop()
    stack.append(height)
    answer += len(stack) -1

print(answer)

