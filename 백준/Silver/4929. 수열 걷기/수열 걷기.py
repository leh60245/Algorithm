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
    arr1 = [0] * 20001
    set1 = set()
    for v in tmp[1:]:
        arr1[v] = 1
        set1.add(v)
    tmp = list(map(int, input().split()))
    arr2 = [0] * 20001
    set2 = set()
    for v in tmp[1:]:
        arr2[v] = 1
        set2.add(v)

    cross_points = set1 & set2
    answer = 0
    sum1, sum2 = 0, 0
    for number in range(-10000, 10001):
        if number in cross_points:
            answer += max(sum1, sum2) + number
            sum1, sum2 = 0, 0
        else:
            if arr1[number]: sum1 += number
            if arr2[number]: sum2 += number
    answer += max(sum1, sum2)
    print(answer)

