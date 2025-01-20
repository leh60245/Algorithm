arr_len = int(input())
arr = list(map(int, input().split()))
x = int(input())

ans = 0

save_int_arr = [0] * x
for i in arr:
    if i >= x:
        continue
    if save_int_arr[x-i]:
        ans += 1
    save_int_arr[i] += 1
print(ans)
