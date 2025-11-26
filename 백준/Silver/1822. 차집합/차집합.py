import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass
input = sys.stdin.readline

nA, nB = map(int, input().split())
arrA = sorted(list(map(int, input().split())))
arrB = sorted(list(map(int, input().split())))


answer = list()
pA, pB = 0, 0
while pA < nA and pB < nB:
    if arrA[pA] < arrB[pB]:
        answer.append(arrA[pA])
        pA += 1
    elif arrA[pA] == arrB[pB]:
        pA += 1
        pB += 1
    else:
        pB += 1

answer = answer + arrA[pA:]

print(len(answer))
print(*answer)