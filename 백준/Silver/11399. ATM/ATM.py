N = int(input())
arr = list(map(int, input().split()))   # 돈을 인출하는데 걸리는 시간

arr.sort()
answer = sum([arr[i] * (N-i) for i in range(N)])
print(answer)
