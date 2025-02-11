N = int(input())
flowers = []
for _ in range(N):
    sm, sd, em, ed = map(int, input().split())
    flowers.append([sm*100+sd, em*100+ed])

ans = 0
max_d = 301
while max_d < 1201:
    tmp = max_d
    for i in range(N):
        if flowers[i][0] <= tmp < flowers[i][1]:
            max_d = max(max_d, flowers[i][1])

    if max_d == tmp:
        ans = 0
        break
    ans += 1
print(ans)