def solve():
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    high = arr[-1]

    check = [0, 0] + [1] * (arr[-1] - 1)
    for idx in range(2, high + 1):
        if check[idx] == 0:
            continue
        q = idx * 2
        while q <= high:
            check[q] = 0
            q += idx

    answer = 0
    for v in arr:
        answer += check[v]
    print(answer)


if __name__ == '__main__':
    solve()
