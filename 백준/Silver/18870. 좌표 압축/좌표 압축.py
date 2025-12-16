import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

N = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(list(set(arr)))
arr2idx = dict()
for i in range(len(sorted_arr)):
    arr2idx[sorted_arr[i]] = i

for v in arr:
    print(arr2idx[v], end=" ")