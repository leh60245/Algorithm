# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    stack = []
    for i in arr[::-1]:
        if not stack:
            stack.append(i)
            continue
        if stack[-1] >= i:
            ans += (stack[-1] - i)
        else:
            stack.append(i)
    print(ans)
