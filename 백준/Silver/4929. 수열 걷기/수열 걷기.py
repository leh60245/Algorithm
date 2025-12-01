import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass
input = sys.stdin.readline

while True:
    tmp = list(map(int, input().split()))
    N = tmp[0]
    if N == 0:
        break
    arr1 = tmp[1:]
    tmp = list(map(int, input().split()))
    M = tmp[0]
    arr2 = tmp[1:]

    answer = 0
    p, q = 0, 0
    sum1, sum2 = 0, 0
    while p < N and q < M:
        if arr1[p] == arr2[q]:
            answer += max(sum1, sum2) + arr1[p]
            sum1, sum2 = 0, 0
            p += 1
            q += 1
        elif arr1[p] < arr2[q]:
            sum1 += arr1[p]
            p += 1
        else:
            sum2 += arr2[q]
            q += 1

    sum1 += sum(arr1[p:])
    sum2 += sum(arr2[q:])

    answer += max(sum1, sum2)
    print(answer)
