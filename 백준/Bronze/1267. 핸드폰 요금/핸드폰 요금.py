cnt = int(input())
s = list(map(int, input().split()))
y=0
m=0
for i in range(cnt):
    y += (s[i]//30 + 1) * 10
for i in range(cnt):
    m += (s[i]//60 + 1) * 15
if y > m:
    print("M", m)
elif y < m:
    print("Y", y)
else:
    print("Y M", y)