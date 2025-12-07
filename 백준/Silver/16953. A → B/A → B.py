import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

n, m = map(int, input().split())

cnt = 1
while n < m:
    if m % 10 == 1:
        m = m // 10
    elif m % 2 == 0:
        m = m // 2
    else:
        break
    cnt += 1

if m == n:
    print(cnt)
else:
    print(-1)
