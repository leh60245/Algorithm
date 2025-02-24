import sys

try:
    sys.stdin = open("input.txt", "r")
except FileNotFoundError:
    pass


def main():
    arr = list()
    arr_len = []
    for _ in range(5):
        tmp = list(map(str, input()))
        arr.append(tmp)
        arr_len.append(len(tmp))

    ans = []
    idx = 0
    while idx < max(arr_len):
        for i in range(5):
            if idx < arr_len[i]:
                ans.append(arr[i][idx])
        idx += 1
    print("".join(map(str, ans)))


if __name__ == "__main__":
    main()
