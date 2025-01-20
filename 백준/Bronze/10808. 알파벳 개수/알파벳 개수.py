import sys
answer = sys.stdin.readline()
answer2 = [0 for _ in range(26)]
for i in answer:
    j = ord(i) - 97
    if j < 0:
        break
    answer2[j] += 1
print(*answer2)