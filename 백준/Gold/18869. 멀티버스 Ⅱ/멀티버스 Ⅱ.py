import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass
input = sys.stdin.readline

m, n = map(int, input().split())
plant = list()
for _ in range(m):
    plant.append(list(map(int, input().split())))

# 정규화
normalize_plant = dict()
for i in range(m):
    sorted_plant = sorted(set(plant[i]))
    rank = {value : idx for idx, value in enumerate(sorted_plant)}

    normalized = tuple(rank[v] for v in plant[i])
    if normalized in normalize_plant:
        normalize_plant[normalized] += 1
    else:
        normalize_plant[normalized] = 1

ans = 0
for cnt in normalize_plant.values():
    ans += cnt * (cnt - 1) // 2

print(ans)
