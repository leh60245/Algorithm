import sys

def foo(n, m, arr):
    en = 0
    tmp = 0
    ans = 0

    for st in range(n):
        while en < n and tmp < m:
            tmp += arr[en]
            en += 1

        if tmp == m:
            ans += 1

        tmp -= arr[st]
    return ans


if __name__ == "__main__":
    try:
        sys.stdin = open("input.txt", "r")  # input.txt가 존재하면 사용
    except FileNotFoundError:
        pass  # 파일이 없으면 (백준 환경) 그냥 넘어감

    input = sys.stdin.readline

    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    print(foo(n, m, arr))
