N, M = map(int, input().split())

num = 1
for _ in range(N):
    line = [str(num + i) for i in range(M)]  # 현재 줄에 들어갈 숫자들
    print(' '.join(line))  # 공백 없이 출력
    num += M  # 다음 줄 시작 숫자 업데이트
