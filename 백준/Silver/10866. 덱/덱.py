import sys
N = int(sys.stdin.readline())
deque = []
for _ in range(N):
    a = list(map(str, sys.stdin.readline().split()))
    if a[0] == "push_front" :
        deque = [int(a[1])] + deque
    elif a[0] == "push_back" :
        deque.append(int(a[1]))
    elif a[0] == "pop_front" :
        print(-1 if deque == [] else deque.pop(0))
    elif a[0] == "pop_back":
        print(-1 if deque == [] else deque.pop())
    elif a[0] == "size":
        print(len(deque))
    elif a[0] == "empty":
        print(1 if deque == [] else 0)
    elif a[0] == "front":
        print(-1 if deque == [] else deque[0])
    else:
        print(-1 if deque == [] else deque[-1])