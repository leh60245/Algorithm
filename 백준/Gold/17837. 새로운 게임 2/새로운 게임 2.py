import sys
from collections import deque

DEBUG = False
try:
    sys.stdin = open("example5.txt", "r")
    DEBUG = True
    print()
except FileNotFoundError:
    pass
input = sys.stdin.readline
'''
NxN 체스판, K개 말, 말은 원판모양으로 하나의 말 위에 다른 말 올릴 수 있음
체스판은 각 칸은 '흰색 0', '빨간색 1', '파란색 2'

게임은 체스판 위에 말 K개 놓음, 말 번호 1~K, 이동방향도 미리 정해짐
이동은 위, 아래, 왼쪽, 오른쪽

[한턴]
1~K 말가지 순서대로 이동하는 것. 한 말이 이동할 때 올려진 말도 함께 이동
말 이동 방향에 있는 칸에 따라서 말의 이동이 다르며, 아래 조건과 같다. 

[조건] A번 말이 이동하려는 칸이
1. [흰색(0)] 그 칸으로 이동. 이동하려는 칸에 말이 이미 있다면 가장 위에 A번 말을 올려 놓는다.
    - A번 말의 위에 다른 말이 있다면 -> A번 말과 위의 말 모두 이동
    [EX] ABC + DE = DEABC
2. [빨간(1)] 이동 후, A번 말과 그 위의 말의 쌓여있는 순서를 반대로 바꾼다.
    [EX] ABC => CBA
    [EX} ABCD + EFG => EFG DCBA
3. [파란(2)] A번 말의 이동 방향을 반대로 하고 한 칸 이동한다. 
    만약 방향을 바꾼 후에 이동하려는 칸이 파란(2)색인 경우, 이동하지 않고 가만히 있는다.
4. [체스판 밖] 파란색과 동일하다.


[종료] 턴 진행 중 말이 4개 이상 쌓이는 순간 게임 종료
'''
N, K = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
chess_board = [[[] for _ in range(N)] for _ in range(N)]  # 위치와 쌓여 있는 순서 저장
chess_info = {}
for num in range(1, K + 1):
    i, j, d = map(int, input().split())
    i, j, d = i - 1, j - 1, d - 1
    ddi, ddj = direction[d]
    chess_board[i][j].append(num)
    chess_info[num] = (i, j, ddi, ddj)


def move_chess(chess_number):
    global grid, chess_board, chess_info
    ci, cj, di, dj = chess_info[chess_number]
    ni, nj = ci + di, cj + dj
    if not (0 <= ni < N and 0 <= nj < N) or grid[ni][nj] == 2:
        ndi, ndj = di * (-1), dj * (-1)
        chess_info[chess_number] = ci, cj, ndi, ndj
        ni, nj = ci + ndi, cj + ndj
        if not (0 <= ni < N and 0 <= nj < N) or grid[ni][nj] == 2:
            return False

    idx = chess_board[ci][cj].index(chess_number)
    chess_board[ci][cj], tmp = chess_board[ci][cj][:idx], chess_board[ci][cj][idx:]
    if grid[ni][nj] == 1:
        tmp = tmp[::-1]
    # 가져온 chess들의 값들을 업데이트 해줘야 함.
    for c_idx in tmp:
        chess_board[ni][nj].append(c_idx)
        _, _, di, dj = chess_info[c_idx]
        chess_info[c_idx] = ni, nj, di, dj

    if len(chess_board[ni][nj]) >= 4:
        return True

    return False

def visual(grid):
    for i in range(N):
        for j in range(N):
            if chess_board[i][j] == []:
                print([0,0,0,0], end=" ")
            else:
                line = [0,0,0,0]
                for k, v in enumerate(chess_board[i][j]):
                    line[k] = v
                print(line, end=' ')
        print()

def main():
    for turn in range(1, 1001):
        if DEBUG:
            print(f"=========== turn {turn} =============")

        for chess in range(1, K + 1):
            is_end = move_chess(chess)
            if is_end:
                print(turn)
                return
        if DEBUG:
            visual(chess_board)

    print(-1)
    return


if __name__ == "__main__":
    main()
