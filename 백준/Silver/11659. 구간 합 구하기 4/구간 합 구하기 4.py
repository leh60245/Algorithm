N, M = map(int, input().split())
arr = list(map(int, input().split()))
sample = [0] # 0, 0~0, 0~1, 0~2
tmp = 0
for i in arr:
    tmp += i
    sample.append(tmp)
for _ in range(M):
    i, j = map(int, input().split())
    i -= 1
    print(sample[j]-sample[i])
