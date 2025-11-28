import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))

result = 0
for v in range(N):
    head, tail = 0, N - 1
    while head < tail:
        if head == v:
            head += 1
            continue
        if tail == v:
            tail -= 1
            continue
        sum = arr[head] + arr[tail]
        if sum < arr[v]:
            head += 1
        elif sum > arr[v]:
            tail -= 1
        else:
            result += 1
            break

print(result)