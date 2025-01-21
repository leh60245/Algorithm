A = input()
B = input()

arr = [0] * 26
for i in A:
    arr[ord(i) - ord('a')] += 1

for i in B:
    arr[ord(i) - ord('a')] -= 1

ans = 0
for k in arr:
    if k != 0:
        ans += abs(k)

print(ans)