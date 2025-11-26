

n = int(input())
arr = sorted(list(map(int, input().split())))
m = int(input())
target = list(map(int, input().split()))


def binary_search(t):
    st = 0
    en = n - 1
    while st <= en:
        mid = (st + en) // 2
        if arr[mid] < t:
            st = mid + 1
        elif arr[mid] > t:
            en = mid - 1
        else:
            return 1

    return 0


for t in target:
    print(binary_search(t))
