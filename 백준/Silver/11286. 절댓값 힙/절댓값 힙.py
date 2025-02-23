import sys
import heapq

def foo(n, arr):
    heap = []
    for i in range(n):
        if arr[i] == 0:
            if heap:
                print(heapq.heappop(heap)[1])
            else:
                print(0)
        else:
            heapq.heappush(heap, (abs(arr[i]), arr[i]))



if __name__ == "__main__":
    try:
        sys.stdin = open("input.txt", "r")
    except FileNotFoundError:
        pass

    input = sys.stdin.readline

    n = int(input())
    arr = [int(input()) for _ in range(n)]
    foo(n, arr)
