import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass
input = sys.stdin.readline

# 25.11.27 17:00
N = int(input())
arr = list(map(int, input().split()))
best = 200000001
answer = 0

head, tail = 0, N - 1
while head < tail:
    sum = arr[head] + arr[tail]
    if abs(sum) < best:
        best = abs(sum)
        answer = sum
    if sum < 0:
        head += 1
    elif sum > 0:
        tail -= 1
    else:
        answer = 0
        break

print(answer)
