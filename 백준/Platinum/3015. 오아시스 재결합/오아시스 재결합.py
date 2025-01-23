N = int(input())    # 1 <= N <= 500,000
stack = []  # (height, count)
ans = 0

for _ in range(N):
    h = int(input())
    c = 1
    while stack and stack[-1][0] <= h:
        ht, cnt = stack.pop()
        if ht == h:
            c += cnt
        ans += cnt

    if stack:
        ans += 1

    stack.append((h, c))

print(ans)