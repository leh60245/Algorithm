import sys
from collections import deque
input = sys.stdin.readline

N = int(input()) # 2,000,000
arr = deque([i for i in range(1, N+1)])
cnt = 0
while len(arr) > 1:
    if cnt == 0:
        arr.popleft()
        cnt = 1
    else:
        arr.append(arr.popleft())
        cnt = 0

print(arr[0])

