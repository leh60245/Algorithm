import sys

def foo(n, s, arr):
    mn = float('inf')
    en = 0
    tot = 0  # 현재 부분 배열의 합

    for st in range(n):
        while en < n and tot < s:
            tot += arr[en]
            en += 1

        if tot >= s:
            mn = min(mn, en - st)

        tot -= arr[st]  

    return mn if mn != float('inf') else 0

if __name__ == "__main__":
    try:
        sys.stdin = open("input.txt", "r")  # input.txt가 존재하면 사용
    except FileNotFoundError:
        pass  # 파일이 없으면 (백준 환경) 그냥 넘어감

    input = sys.stdin.readline

    n, s = map(int, input().split())
    arr = list(map(int, sys.stdin.readline().split()))

    print(foo(n, s, arr))
