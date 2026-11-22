dancers = {"ChongChong"}


def solve() -> None:
    n_line = input()
    if not n_line:
        print(0)
        return

    N = int(n_line)

    for _ in range(N):
        a, b = map(str, input().split())
        if a not in dancers and b not in dancers:
            pass
        else:
            dancers.add(a)
            dancers.add(b)

    print(len(dancers))


if __name__ == "__main__":
    solve()