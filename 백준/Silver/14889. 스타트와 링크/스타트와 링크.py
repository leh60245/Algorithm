import sys
from itertools import combinations

try:
    sys.stdin = open("example3.txt", "r")
except FileNotFoundError:
    pass
input = sys.stdin.readline
# N(짝수 사람) 2팀 나눔
# 번호 1~N 배정, i번과 j번 사람 시너지 = Sij
# 팀 능력치 = 모든 Sij, Sij != Sji
# i와 j 사람이 같은 팀에 있다면 -> 팀 능력치 += Sij+Sji

# [목표] 능력치 차이 최소로 하기
N = int(input())
grid = list()
for _ in range(N):
    tmp = list(map(int, input().split()))
    grid.append(tmp)


def main():
    ans = float('inf')
    for com1 in combinations([i for i in range(N)], N // 2):
        com2 = [i for i in range(N) if i not in com1]
        first_power = 0
        second_power = 0
        for i, j in combinations(com1, 2):
            first_power += grid[i][j] + grid[j][i]
        for i, j in combinations(com2, 2):
            second_power += grid[i][j] + grid[j][i]
        ans = min(ans, abs(first_power - second_power))

    print(ans)


if __name__ == "__main__":
    main()
