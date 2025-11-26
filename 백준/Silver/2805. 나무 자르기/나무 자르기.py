import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass
input = sys.stdin.readline

n, m = map(int, input().split())
tree = sorted(list(map(int, input().split())))

def binary_search():
    st = 0
    en = tree[-1]
    ans = 0

    while st <= en:
        mid = (st + en) // 2
        if mid == 0:
            return 0

        sum_heigh = 0
        for v in tree:
            sum_heigh += max(v - mid, 0)

        if sum_heigh >= m:
            ans = mid
            st = mid + 1
        else:
            en = mid - 1

    return ans

print(binary_search())