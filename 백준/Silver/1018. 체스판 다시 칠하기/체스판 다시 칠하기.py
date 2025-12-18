import sys

def solve():
    # 1. 입력 받기
    # N: 행의 개수, M: 열의 개수
    N, M = map(int, sys.stdin.readline().split())
    
    # 보드 상태 입력 받기 (리스트의 리스트 형태)
    board = []
    for _ in range(N):
        board.append(sys.stdin.readline().strip())

    # 다시 칠해야 하는 정사각형의 최소 개수를 저장할 변수
    # 최악의 경우 64칸을 모두 칠해야 하므로 64보다 큰 값이나 64로 초기화해도 됩니다.
    min_repaints = 64

    # 2. 가능한 모든 8x8 체스판의 시작점 탐색
    # 행은 0부터 N-8까지, 열은 0부터 M-8까지 가능합니다.
    for i in range(N - 7):
        for j in range(M - 7):
            
            w_start_count = 0  # 왼쪽 위가 'W'로 시작할 때 다시 칠해야 하는 수
            b_start_count = 0  # 왼쪽 위가 'B'로 시작할 때 다시 칠해야 하는 수

            # 3. 해당 시작점부터 8x8 크기 내부를 확인
            for r in range(i, i + 8):
                for c in range(j, j + 8):
                    current_cell = board[r][c]
                    
                    # 행 번호(r)와 열 번호(c)의 합이 짝수인지 홀수인지로 체스판 패턴 확인
                    if (r + c) % 2 == 0:
                        # (r+c)가 짝수면 시작점과 같은 색이어야 함
                        if current_cell != 'W': w_start_count += 1
                        if current_cell != 'B': b_start_count += 1
                    else:
                        # (r+c)가 홀수면 시작점과 다른 색이어야 함
                        if current_cell != 'B': w_start_count += 1
                        if current_cell != 'W': b_start_count += 1
            
            # 4. 현재 8x8 구역에서 더 적게 칠하는 횟수를 선택하여 최솟값 갱신
            current_min = min(w_start_count, b_start_count)
            min_repaints = min(min_repaints, current_min)

    # 결과 출력
    print(min_repaints)

if __name__ == "__main__":
    solve()