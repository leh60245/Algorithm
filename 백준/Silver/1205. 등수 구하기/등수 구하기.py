# import sys
#
# sys.stdin = open("input.txt")

n, new_score, p = map(int, input().split())
if n == 0:
    print(1)
    exit()

score = list(map(int, input().split()))
rank = 1
tmp = 0
for i in range(len(score)):
    if score[i] > new_score:
        rank += 1
    elif score[i] == new_score:
        tmp += 1
    else:
        break

if rank + tmp > p:
    print(-1)
else:
    print(rank)