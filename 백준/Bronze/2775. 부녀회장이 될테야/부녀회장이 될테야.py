import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

T = int(input())
for _ in range(T):
    k = int(input()) # k층
    n = int(input()) # n호

    arr = [i for i in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            arr[j] = arr[j] + arr[j-1]

    print(arr[n-1])