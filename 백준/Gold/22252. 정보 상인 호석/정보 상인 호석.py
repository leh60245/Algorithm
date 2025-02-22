import sys
import heapq

def process_queries(q, queries):
    gorillas = {}  # 고릴라별 정보 저장 (딕셔너리)
    total_cost = 0  # 호석이가 구매한 정보 가치 총합

    for query in queries:
        data = query.split()
        command, name = int(data[0]), data[1]

        if command == 1:  # 고릴라가 새로운 정보를 획득하는 경우
            k = int(data[2])
            values = list(map(int, data[3:3 + k]))

            if name not in gorillas:
                gorillas[name] = []
            for value in values:
                heapq.heappush(gorillas[name], -value)  # 최대 힙 구현 (-를 붙여 저장)

        elif command == 2:  # 호석이가 정보 구매하는 경우
            b = int(data[2])
            if name in gorillas:
                for _ in range(b):
                    if gorillas[name]:  # 구매 가능한 정보가 있는 경우
                        total_cost += -heapq.heappop(gorillas[name])  # 최대값 꺼내기
                    else:
                        break  # 더 이상 정보가 없으면 종료

    return total_cost  # 총 구매 금액 반환

if __name__ == "__main__":
    try:
        sys.stdin = open("input.txt", "r")
    except FileNotFoundError:
        pass

    input = sys.stdin.read
    data = input().split("\n")

    Q = int(data[0])  # 쿼리 개수
    queries = data[1:Q + 1]  # 나머지 Q개의 줄

    print(process_queries(Q, queries))