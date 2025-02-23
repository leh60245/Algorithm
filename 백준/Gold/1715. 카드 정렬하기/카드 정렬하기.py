import sys
import heapq

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    input = sys.stdin.readline

def main():
    n = int(input())
    heap = []
    for _ in range(n):
        heapq.heappush(heap, int(input()))

    if n == 1:
        print(0)
        return

    ans = 0
    while len(heap) > 1:
        tmp = heapq.heappop(heap) + heapq.heappop(heap)
        ans += tmp
        heapq.heappush(heap, tmp)
    print(ans)
    return


if __name__ == "__main__":
    main()
