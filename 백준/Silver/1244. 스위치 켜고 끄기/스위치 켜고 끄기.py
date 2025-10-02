# import sys
#
# sys.stdin = open("input.txt")

n = int(input())
switch = list(map(int, input().split()))
m = int(input())
student = list()
for _ in range(m):
    student.append(tuple(map(int, input().split())))

for gender, num in student:
    if gender == 1:  # 남학생
        for idx in range(num, n+1, num):
            idx -= 1
            switch[idx] = 1 - switch[idx]
    else:
        num -= 1
        switch[num] = (switch[num] + 1) % 2
        dir = 1
        while num - dir >= 0 and num + dir < n and switch[num - dir] == switch[num + dir]:
            switch[num - dir] = switch[num + dir] = 1 - switch[num + dir]
            dir += 1

start = 0
end = 20
while True:
    if end >= n:
        print(*switch[start:n])
        break
    print(*switch[start:end])
    start += 20
    end += 20
