N = int(input())
arr_min = []
arr_plu = []
for _ in range(N):
    c = int(input())
    if c <= 0:
        arr_min.append(c)
    else:
        arr_plu.append(c)

arr_min.sort()
arr_plu.sort()
ans = 0
for i in range(0, len(arr_min), 2):
    if i+1 < len(arr_min):
        ans += max(arr_min[i] * arr_min[i+1], arr_min[i] + arr_min[i+1])
    else:
        ans += arr_min[i]
for i in range(len(arr_plu)-1, -1, -2):
    if i-1 >= 0:
        ans += max(arr_plu[i] * arr_plu[i-1], arr_plu[i] + arr_plu[i-1])
    else:
        ans += arr_plu[i]

print(ans)