import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

T = int(input())
for _ in range(T):
    N = int(input())
    stickers = list()
    for _ in range(2):
        stickers.append(list(map(int, input().split())))

    dp = [[float('inf') for _ in range(N + 1)] for _ in range(2)]
    dp[0][0] = 0
    dp[1][0] = 0
    dp[0][1] = stickers[0][0]
    dp[1][1] = stickers[1][0]

    for j in range(2, N + 1):
        for i in range(2):
            dp[i][j] = stickers[i][j-1] + max(dp[(i + 1) % 2][j - 2], dp[(i + 1) % 2][j - 1])

    print(max(max(dp[0][-3:]), max(dp[1][-3:])))