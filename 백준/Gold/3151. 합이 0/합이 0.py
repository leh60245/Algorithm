import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass
input = sys.stdin.readline

# 25.11.27 16:20
N = int(input())
power = sorted(list(map(int, input().split())))
answer = 0

for p1 in range(N - 2):
    p2, p3 = p1 + 1, N - 1
    while p2 < p3:
        sum = power[p1] + power[p2] + power[p3]
        if sum < 0:
            p2 += 1
        elif sum > 0:
            p3 -= 1
        else:
            if power[p2] == power[p3]:
                cnt = p3 - p2 + 1
                answer += cnt * (cnt - 1) // 2
                break
            else:
                tmp_p2 = p2 + 1
                cnt_p2 = 1
                while tmp_p2 < p3:
                    if power[p2] == power[tmp_p2]:
                        cnt_p2 += 1
                        tmp_p2 += 1
                    else:
                        break
                tmp_p3 = p3 - 1
                cnt_p3 = 1
                while p2 < tmp_p3:
                    if power[tmp_p3] == power[p3]:
                        cnt_p3 += 1
                        tmp_p3 -= 1
                    else:
                        break
                answer += cnt_p2 * cnt_p3
                p2 = tmp_p2
                p3 = tmp_p3

print(answer)
