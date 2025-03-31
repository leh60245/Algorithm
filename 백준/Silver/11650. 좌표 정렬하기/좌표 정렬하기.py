N = int(input())
arr = []
for _ in range(N):
    arr.append(tuple(map(int, input().split())))
arr.sort()
for i, j in arr:
    print(i, j)