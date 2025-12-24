# BOJ_20044
# Project Teams

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = sorted(list(map(int, inp().split())))
    res = 100000 * 2
    for i in range(n):
        tmp = arr[i] + arr[n * 2 - i - 1]
        res = min(res, tmp)
    print(res)


if __name__ == "__main__":
    main()
