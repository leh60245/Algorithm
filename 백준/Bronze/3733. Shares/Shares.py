import sys

for line in sys.stdin:
    if not line.strip():  # 빈 줄 예외 처리
        continue
    try:
        N, S = map(int, line.strip().split())
        print(S // (N + 1))  # 본인 포함 N+1명으로 나눔
    except:
        continue  # 예외 발생 시 무시하고 다음 줄
