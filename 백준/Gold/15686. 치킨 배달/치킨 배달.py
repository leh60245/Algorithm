import sys
from collections import deque
from itertools import combinations

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

input = sys.stdin.readline
n, m = map(int, input().split())
grid = []
home = []
chicken = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 2:
            chicken.append((i, j))
        elif tmp[j] == 1:
            home.append((i, j))
    grid.append(tmp)

def oob(i, j):
    return not (0 <= i < n and 0 <= j < n)

def calculate_distance(hi, hj, com):
    min_dist = float('inf')
    for i, j in com:
        min_dist = min(min_dist, abs(i-hi) + abs(j-hj))
    return min_dist


def main():
    answer = float('inf')
    for com in combinations(chicken, m):
        home_to_chicken = 0
        for hi, hj in home:
            home_to_chicken += calculate_distance(hi, hj, com)
        answer = min(answer, home_to_chicken)
    print(answer)


if __name__ == "__main__":
    main()
