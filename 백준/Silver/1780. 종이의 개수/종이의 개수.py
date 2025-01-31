N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

def re(n, si, sj):
    if n == 0:
        return 0, 0, 0

    tmp = None
    allSame = True
    for i in range(si, si+n):
        for j in range(sj, sj+n):
            if tmp is None:
                tmp = arr[i][j]
                continue
            if tmp != arr[i][j]:
                allSame = False
                break
        if not allSame:
            break

    if allSame:
        if tmp == -1:
            return 1, 0, 0
        elif tmp == 0:
            return 0, 1, 0
        else: # tmp == 1
            return 0, 0, 1

    x, y, z = 0, 0, 0
    for p in range(3):
        for q in range(3):
            x1, y1, z1 = re(n//3, si + (n//3)*p, sj + (n//3)*q)
            x += x1
            y += y1
            z += z1

    return x, y, z

print(*re(N, 0, 0), sep= "\n")