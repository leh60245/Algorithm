import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass
input = sys.stdin.readline

# 25.11.27 15:52
N = int(input())
arr = list(map(int, input().split()))

head = 0
tail = N - 1
answer = (arr[head], arr[tail])
best = 2000000000

while head < tail:
    tmp = arr[head] + arr[tail]
    if abs(tmp) < best:
        answer = (arr[head], arr[tail])
        best = abs(tmp)
    if tmp > 0:
        tail -= 1
    elif tmp < 0:
        head += 1
    else:
        break

print(*answer)
