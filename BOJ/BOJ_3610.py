# BOJ_3610
# Graveyard

import sys

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    tmp1 = []
    tmp2 = []
    for i in range(n):
        tmp1.append((10000 / n) * i)

    for i in range(n + m):
        tmp2.append((10000 / (n + m)) * i)

    res = sum((min(abs(i - j) for j in tmp2) for i in tmp1))

    print(f"{res:.4f}")


if __name__ == "__main__":
    main()
