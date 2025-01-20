import math
n = input()
arr = [0] * 9
for i in n:
    if i == '9' or i == '6':
        arr[6] += 0.5
    else:
        arr[int(i)] += 1

print(math.ceil(max(arr)))