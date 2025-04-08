import sys

DEBUG = False
try:
    sys.stdin = open("example4.txt", "r")
    DEBUG = True
    print()
except FileNotFoundError:
    pass
input = sys.stdin.readline
"""
RxC 격자판, 한 칸에 최대 한 마리, 상어는 크기와 속도 가짐
낚시왕은 -1 index에서 R index로 가면 끝

[1초동안 일어나는 일]
1. 낚시왕 오른쪽 이동
2. 낚시왕이 있는 열에서 행 번호가 가장 작은 상어 잡음. 
    상어를 잡으면 상어는 사라짐
3. 상어가 이동

[상어의 이동]
 - 주어진 속도로 이동, 속도 단위는 칸/초 
 - 이동하려는 칸이 격자판 경계인 경우, 
    -> 방향을 반대로 바꿔 속도 유지한채 이동
 - 이동을 마친 뒤 한 칸에 상어가 두 마리 이상 있을 수 있다.
    -> 이때, 크기가 큰 상어가 나머지 상어 모두 잡아먹는다.
    
[목표] 낚시왕이 잡은 상어 '크기'의 합을 구하자.

[주어진 조건]
두 상어는 같은 크기를 갖지 않는다.
하나의 칸에 둘 이상의 상어가 있는 경우는 없다.
"""
R, C, M = map(int, input().split())
sharks = [[[] for _ in range(C)] for _ in range(R)]
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
for _ in range(M):
    # i, j, speed, direction, size
    i, j, s, d, z = map(int, input().split())
    i, j, d = i - 1, j - 1, d - 1
    di, dj = direction[d]
    sharks[i][j].append((s, di, dj, z))


def catch_shark(col):
    global sharks
    for row in range(R):
        if sharks[row][col]:
            _, _, _, z = sharks[row][col][0]
            sharks[row][col] = []
            return z
    return 0


def move_shark():
    new_sharks = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if not sharks[i][j]:
                continue
            for s, di, dj, z in sharks[i][j]:
                if di == 0:  # 좌우 col을 옮겨 다님
                    s %= (C - 1) * 2
                    cnt = 0
                    cj = j
                    while cnt < s:
                        nj = cj + dj
                        if nj < 0:
                            nj = 1
                            dj *= -1
                        elif nj >= C:
                            nj = C - 2
                            dj *= -1
                        cj = nj
                        cnt += 1
                    new_sharks[i][cj].append((s, di, dj, z))
                else:  # 상하 col line에 있음
                    s %= (R - 1) * 2
                    cnt = 0
                    ci = i
                    while cnt < s:
                        ni = ci + di
                        if ni < 0:
                            ni = 1
                            di *= -1
                        elif ni >= R:
                            ni = R - 2
                            di *= -1
                        ci = ni
                        cnt += 1
                    new_sharks[ci][j].append((s, di, dj, z))

    for i in range(R):
        for j in range(C):
            if not new_sharks[i][j] or len(new_sharks[i][j]) == 1:
                continue
            new_sharks[i][j].sort(key=lambda x: x[3])
            new_sharks[i][j] = [new_sharks[i][j][-1]]

    return new_sharks

def visual(col):
    print(f"========== col-{col} ===========")
    for i in range(R):
        for j in range(C):
            if not sharks[i][j]:
                print("0", end=" ")
            else:
                _, _, _, z = sharks[i][j][0]
                print(f"{z}", end=" ")
        print()

def main():
    global sharks
    sum_size = 0
    if DEBUG:
        visual(-1)
    for col in range(C):
        sum_size += catch_shark(col)
        sharks = move_shark()
        if DEBUG:
            visual(col)

    print(sum_size)


if __name__ == "__main__":
    main()
