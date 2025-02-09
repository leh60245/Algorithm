N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)  # 10,000 -> 0
max_weight = 0
for i in range(N):
    tmp = arr[i] * (i+1)
    max_weight = max(max_weight, tmp)
print(max_weight)