N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
ans = [0, 0]

def check(si, sj, n):
    for i in range(si, si+n):
        for j in range(sj, sj+n):
            if arr[i][j] != arr[si][sj]:
                return False

    return True

def re(si, sj, n):
    if n == 0:
        return 0

    if check(si, sj, n):
        ans[arr[si][sj]] += 1
        return 0

    for i in range(2):
        for j in range(2):
            re(si+(n//2)*i, sj+(n//2)*j, n//2)

    return 0

re(0, 0, N)
print(*ans, sep='\n')