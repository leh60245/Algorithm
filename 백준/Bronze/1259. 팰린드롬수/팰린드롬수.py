import sys
input = sys.stdin.readline

while True:
    num = input().strip()
    if num == "0":  # 종료 조건
        break
    
    # 팰린드롬 판별
    if num == num[::-1]:
        print("yes")
    else:
        print("no")
