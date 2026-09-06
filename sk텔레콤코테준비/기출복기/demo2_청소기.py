from collections import deque

N = 5
# 벽: (r1,c1,r2,c2) = 두 인접 칸 '사이'가 막혀 있다
walls = [(0,2,0,3),(1,2,1,3),(2,2,2,3),(3,2,3,3)]
blocked = set()
for r1,c1,r2,c2 in walls:
    blocked.add(((r1,c1),(r2,c2)))
    blocked.add(((r2,c2),(r1,c1)))   # 양방향 모두 막기

def bfs(src):
    dist = [[-1]*N for _ in range(N)]
    dist[src[0]][src[1]] = 0
    q = deque([src])
    while q:
        r,c = q.popleft()
        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr,nc = r+dr, c+dc
            if not (0 <= nr < N and 0 <= nc < N): continue
            if ((r,c),(nr,nc)) in blocked: continue     # 벽 통과 불가
            if dist[nr][nc] != -1: continue
            dist[nr][nc] = dist[r][c] + 1
            q.append((nr,nc))
    return dist

def grid(g):
    return "\n".join("  " + " ".join(f"{v:2}" for v in row) for row in g)

src = (0,0)
man = [[abs(r-src[0]) + abs(c-src[1]) for c in range(N)] for r in range(N)]
bfsd = bfs(src)
print("[E] 벽은 col2 | col3 사이 (0~3행). 청소기 (0,0)")
print("  맨해튼 거리:");  print(grid(man))
print("  실제 BFS 거리:"); print(grid(bfsd))
print("  => 오른쪽 위 칸은 맨해튼 3~4인데 실제로는 7~9. 맨해튼으로 풀면 전부 틀림\n")

# 두 청소기가 처음 '만나는' k 찾기
A, B = (0,0), (0,4)
da, db = bfs(A), bfs(B)
first = min(max(da[r][c], db[r][c])
            for r in range(N) for c in range(N)
            if da[r][c] >= 0 and db[r][c] >= 0)
print(f"[F] 청소기 {A}, {B}")
print(f"  두 범위가 처음 겹치는 k = {first}  ->  겹침 0 을 유지하는 최대 k = {first-1}")
for k in range(first-1, first+1):
    ov = sum(1 for r in range(N) for c in range(N)
             if 0 <= da[r][c] <= k and 0 <= db[r][c] <= k)
    print(f"  k={k} 일 때 겹치는 칸 수 = {ov}")
