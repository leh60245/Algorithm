def solve():
    answer = 0
    N = int(input())
    if N == 1 or N == 0:
        print(N)
        return
    arr = [0] * (N + 1)
    arr[0] = 0
    arr[1] = 1
    for i in range(2, N+1):
        arr[i] = arr[i-1] + arr[i-2]

    print(arr[N])

if __name__ == '__main__':
    solve()

