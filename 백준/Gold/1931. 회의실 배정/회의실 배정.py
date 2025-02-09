# import sys
# sys.stdin = open("input.txt", "r")
N = int(input())
times = []
for _ in range(N):
    times.append(tuple(map(int, input().split())))
times.sort(key=lambda x: (x[1], x[0]))

ans = 0
start_t = 0
for i in range(N):
    if start_t > times[i][0]:
        continue
    ans += 1
    start_t = times[i][1]

print(ans)