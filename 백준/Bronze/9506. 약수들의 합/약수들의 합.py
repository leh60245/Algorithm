import sys
import math

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass

input = sys.stdin.readline


def main():
    while True:
        n = int(input())
        if n == -1:
            break
        save = {1}
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                save.add(i)
                save.add(n//i)
        save = sorted(save)
        if sum(save) == n:
            print(f"{n} =", " + ".join(map(str, save)))
        else:
            print(f"{n} is NOT perfect.")


if __name__ == "__main__":
    main()
