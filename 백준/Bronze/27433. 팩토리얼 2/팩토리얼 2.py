n = int(input())
ans = 1
tmp = 1
while tmp <= n:
    ans *= tmp
    tmp += 1

print(ans)