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
NxN 격자, 구역을 5개 선거구로 나눠야 하고, 각 구역은 하나의 선거구에 포함되어야 한다.
선거구는 구역을 적어도 하나 포함해야 하고, 한 선거구에 포함되어 있는 구역은 모두 연결되어야 한다.
구역 A에 인접한 인접한 구역을 통해서 구역 B로 갈 수 있을 때, 두 구역은 연결되어 있다고 한다.
중간에 통하는 인접한 구역은 0개 이상이어야 하고, 모두 같은 선거구에 포함된 구역이어야 한다.

[선거구 나누는 방법]
1. 기준점 (x, y)와 경계 길이 d1, d2를 정한다. 
2. 다음 칸은 경계선이다.
    1번 경계선: (x,y) += (1, -1) .. (d1, -d1)
    2번 경계선: += (1, 1) ... (d2, d2)
    3: (x+d1, y-d1) += (1, 1), ... , (d2, d2)
    4: (x+d2, y+d2) += (1, -1), ... , (d1, -d1)
3. 경계선과 경꼐선의 안에 포함되어있는 곳은 5번 선거구다.
4. 5번 선거구에 포함되지 않은 구역 (r, c)의 선거구 번호는 다음 기준을 따른다.
    1번 선거구: r < x+d1, c <= y, 1번 경계선 위
    2번 선거구: r <= x+d2, y < c <= N, 2번 경계선 위
    3번 선거구: x+d1 <= r < N, c < y-d1+d2, 3번 경계선 아래
    4번 선거구: x+d2 < r < N, y-d1+d2 <= c < N, 4번 경계선 아래
    
[목표] 선거구를 나누는 방법 중, 인구가 가장 많은 선거구 - 가장 적은 선거구의 최솟값을 구하자.

(d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N)
'''
N = int(input())
grid = []
sum_all = 0
for _ in range(N):
    tmp = list(map(int, input().split()))
    grid.append(tmp)
    sum_all += sum(tmp)


def find_edge(si, sj, d1, d2):
    edges = [set() for _ in range(4)]
    all_edges = set()
    for e in range(4):
        if e == 0:
            ci, cj, di, dj, max_cnt = si, sj, 1, -1, d1
        elif e == 1:
            ci, cj, di, dj, max_cnt = si, sj, 1, 1, d2
        elif e == 2:
            ci, cj, di, dj, max_cnt = si + d1, sj - d1, 1, 1, d2
        else:
            ci, cj, di, dj, max_cnt = si + d2, sj + d2, 1, -1, d1
        edges[e].add((ci, cj))
        all_edges.add((ci, cj))
        cnt = 0
        while cnt < max_cnt:
            ci, cj = ci + di, cj + dj
            if DEBUG:
                if not (0<=ci<N and 0<=cj<N):
                    print(f"{(ci, cj)} is out of box")
                    return 0, 0
            edges[e].add((ci, cj))
            all_edges.add((ci, cj))
            cnt += 1
    return edges, all_edges

def visual(grid, edges):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in edges:
                print("*", end=" ")
            else:
                print(grid[i][j], end=" ")
        print()




def main():
    answer = float('inf')
    for i in range(N-2):
        for j in range(1, N-1):
            for d1 in range(1, N-1):
                for d2 in range(1, N-1):
                    if i+d1+d2 < N and 0 <= j-d1 and j+d2 < N:
                        if DEBUG:
                            visual_grid = [[0 for _ in range(N)] for _ in range(N)]
                        edges, all_edges = find_edge(i, j, d1, d2)

                        lands = [0 for _ in range(5)]
                        for ci in range(i+d1):
                            for cj in range(j+1):
                                if (ci, cj) in all_edges:
                                    break
                                lands[0] += grid[ci][cj]
                                if DEBUG:
                                    if visual_grid[ci][cj]:
                                        print(f"error) 1번 선거구를 그리는데 이미 {(ci, cj)} 자리에 {visual_grid[ci][cj]}")
                                        return
                                    visual_grid[ci][cj] = 1
                        for ci in range(i+d2+1):
                            for cj in range(N-1, j, -1):
                                if (ci, cj) in all_edges:
                                    break
                                lands[1] += grid[ci][cj]
                                if DEBUG:
                                    if visual_grid[ci][cj]:
                                        print(
                                            f"error) 2번 선거구를 그리는데 이미 {(ci, cj)} 자리에 {visual_grid[ci][cj]}")
                                        return
                                    visual_grid[ci][cj] = 2
                        for ci in range(i+d1, N):
                            for cj in range(j-d1+d2):
                                if (ci, cj) in all_edges:
                                    break
                                lands[2] += grid[ci][cj]
                                if DEBUG:
                                    if visual_grid[ci][cj]:
                                        print(f"error) 3번 선거구를 그리는데 이미 {(ci, cj)} 자리에 {visual_grid[ci][cj]}")
                                        return
                                    visual_grid[ci][cj] = 3
                        for ci in range(i+d2+1, N):
                            for cj in range(N-1, j-d1+d2-1, -1):
                                if (ci, cj) in all_edges:
                                    break
                                lands[3] += grid[ci][cj]
                                if DEBUG:
                                    if visual_grid[ci][cj]:
                                        print(
                                            f"error) 4번 선거구를 그리는데 이미 {(ci, cj)} 자리에 {visual_grid[ci][cj]}")
                                        return
                                    visual_grid[ci][cj] = 4
                        lands[4] = sum_all - sum(lands)
                        tmp = max(lands) - min(lands)
                        answer = min(tmp, answer)
                        if answer == 0:
                            print(0)
                            return
                        if DEBUG:
                            print(i, j, d1, d2)
                            print(all_edges)
                            print(tmp)
                            visual(visual_grid, all_edges)
                            print()

    print(answer)


if __name__ == "__main__":
    main()
