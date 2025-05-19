import math

# 진약수의 합을 구하는 함수
def proper_divisor_sum(n):
    total = 1  # 1은 항상 약수
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total if n != 1 else 0  # 1은 약수가 없으므로 0 리턴

# 입력 받기
T = int(input())
nums = list(map(int, input().split()))

# 각 수에 대해 판단
for n in nums:
    sum_div = proper_divisor_sum(n)
    if sum_div == n:
        print("Perfect")
    elif sum_div < n:
        print("Deficient")
    else:
        print("Abundant")
