import sys
import heapq

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    input = sys.stdin.readline


def main():
    n = int(input())
    heap = list()
    for _ in range(n):
        cmd = int(input())
        if cmd == 0:
            if heap:
                print(heapq.heappop(heap))
            else:
                print(0)
        else:
            heapq.heappush(heap, cmd)


if __name__ == "__main__":
    main()
