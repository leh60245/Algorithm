import sys
from collections import deque

def process_keystrokes(n, cases):
    results = []
    
    for s in cases:
        left = deque()   # 커서 왼쪽 문자들
        right = deque()  # 커서 오른쪽 문자들

        for cmd in s:
            if cmd == '<':
                if left:
                    right.appendleft(left.pop())  # 왼쪽에서 하나 빼서 오른쪽으로 이동
            elif cmd == '>':
                if right:
                    left.append(right.popleft())  # 오른쪽에서 하나 빼서 왼쪽으로 이동
            elif cmd == '-':
                if left:
                    left.pop()  # 왼쪽에서 하나 삭제
            else:
                left.append(cmd)  # 커서 위치에서 문자 삽입

        results.append("".join(left) + "".join(right))  # 최종 문자열 생성

    return "\n".join(results)  # 개행 문자로 결과 연결 후 반환

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split("\n")
    
    n = int(data[0])  # 테스트 케이스 개수
    cases = data[1:n+1]  # 문자열 입력 리스트

    print(process_keystrokes(n, cases))
