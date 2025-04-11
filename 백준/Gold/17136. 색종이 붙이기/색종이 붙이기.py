import sys

DEBUG = False
try:
    sys.stdin = open("example4.txt", "r")
    DEBUG = True
    print()
except FileNotFoundError:
    pass
input = sys.stdin.readline
'''
색종이 종류 5가지 : 1x1 ~ 5x5
각 종류의 색종이 5개씩 가짐
색종이를 10x10 크기의 종이 위에 붙이려 함
각 칸에는 0또는 1이 적힘. 1이 적힌 칸은 모두 색종이로 덮여져야 한다.
색종이가 종이 경계 밖으로 나가면 안되고, 겹쳐도 안 된다. 또 칸의 경계와 일치해야 한다.
0이 적힌 칸에는 색종이가 있으면 안된다. 

[목표] 1이 적힌 모든 칸을 붙이는데 필요한 색종이의 최소 개수를 구하자.
[조건] 모든 1을 덮는데 필요한 색종이 최소 개수를 출력한다.
단, 불가능 할 경우 -1을 출력한다.
'''
N = 10
grid = []
all_space = 0
for _ in range(N):
    tmp = list(map(int, input().split()))
    all_space += sum(tmp)
    grid.append(tmp)
visited = [[0 for _ in range(N)] for _ in range(N)]
ans = 25 + 1

'''
0, 0, 3

0 2 => si+s, sj+size-1
1 2
2 2

'''

def visual_grid(grid):
    if not DEBUG:
        return
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                if visited[i][j]:
                    print(visited[i][j], end= " ")
                else:
                    print("x", end=" ")
            else:
                print(0, end=" ")
        print()


def check_grid(si, sj, size):
    for i in range(si, si + size):
        for j in range(sj, sj + size):
            if grid[i][j] == 0:
                return False
    return True

def check_visited(si, sj, size):
    for i in range(si, si + size):
        for j in range(sj, sj + size):
            if visited[i][j]:
                return False
    return True



def attach(si, sj, size):
    global visited
    for i in range(si, si + size):
        for j in range(sj, sj + size):
            visited[i][j] = size


def detach(si, sj, size):
    global visited
    for i in range(si, si + size):
        for j in range(sj, sj + size):
            visited[i][j] = 0


def dfs(si, sj, can_used, cnt_use, left_space, depth):
    global ans
    if DEBUG:
        print(f"======= depth {depth} =========")
        print(f"used paper {can_used}")
        visual_grid(grid)

    if cnt_use >= ans:
        return
    if left_space == 0:
        ans = min(cnt_use, ans)
        return
    for i in range(si, N):
        for j in range(N):
            if si == i and j < sj:
                continue
            if grid[i][j] == 1 and not visited[i][j]:
                for s in range(5,0,-1):
                    if can_used[s - 1] == 0:
                        # 색종이가 없는 경우는 다음 색종이를 확인하면 된다.
                        continue
                    if i + s > N or j + s > N:
                        continue
                    if not check_grid(i, j, s):
                        continue
                    if not check_visited(i, j, s):
                        continue

                    attach(i, j, s)
                    can_used[s - 1] -= 1
                    dfs(i, j + s, can_used, cnt_use + 1, left_space - s * s, depth+1)
                    can_used[s - 1] += 1
                    detach(i, j, s)
                return
    print(f"END depth {depth}")

def main():
    can_use = [5] * 5
    dfs(0, 0, can_use, 0, all_space, 0)
    if ans == 26:
        print(-1)
        return
    print(ans)
    return


if __name__ == "__main__":
    main()
