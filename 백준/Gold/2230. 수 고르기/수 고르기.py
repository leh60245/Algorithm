import sys

def min_difference(n, m, arr):
    arr.sort()
    mn = float('inf')
    en = 0

    for st in range(n):
        while en < n and arr[en] - arr[st] < m:
            en += 1
        if en < n:  # en이 범위를 벗어나지 않을 경우만 최소값 갱신
            mn = min(mn, arr[en] - arr[st])

    return mn if mn != float('inf') else 0

if __name__ == "__main__":
    # with open("input.txt", "r") as file:
    #     data = list(map(int, file.read().split()))

    input = sys.stdin.read
    data = list(map(int, input().split()))
    
    n, m, *arr = data  # 리스트 언패킹

    print(min_difference(n, m, arr))
