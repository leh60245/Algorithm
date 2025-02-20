import sys
# sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
arr = list()
for _ in range(N):
    arr.append(int(input()))
arr.sort()

p, q = 0, 0
ans = sys.maxsize
while q < N and p < N:
    tmp = arr[q] - arr[p]
    if tmp < M:
        q += 1
    else:
        p += 1
        ans = min(ans, tmp)

print(ans)